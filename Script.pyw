import smtplib
import socket
import datetime
import time
import configparser


class Config:
    def __init__(self, config_file_name):
        self.SENDER_ADDRESS = ''
        self.SENDER_PASSWORD = ''
        self.RECEIVER_ADDRESS = ''
        self.PC_NAME = ''
        self.HOST = ''
        self.PORT = 0
        self.config_file = configparser.ConfigParser()
        self.config_file_name = config_file_name

    def read_in(self):
        err_msg = 'none'
        try:
            self.config_file.read(self.config_file_name)
        except:
            err_msg = 'Error : Configuration file not found. Please run setup again.'

        try:
            self.SENDER_ADDRESS = self.config_file['SENDER']['address']
            self.SENDER_PASSWORD = self.config_file['SENDER']['password']
            self.HOST = self.config_file['SENDER']['host']
            self.PORT = int(self.config_file['SENDER']['port'])
        except:
            err_msg = 'Error : Sender information not found. Please run setup again.'

        try:
            self.RECEIVER_ADDRESS = self.config_file['RECEIVER']['address']
        except:
            err_msg = 'Error : Receiver information not found. Please run setup again'

        try:
            self.PC_NAME = self.config_file['MISC']['pc_name']
        except:
            pass
        return err_msg


# method to check if there is internet connection
def is_connected():
    host = '8.8.8.8'
    port = 53
    timeout = 3
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex.message)
        pass
    return False


def log_failure():
    exit()


def main():
    timeout_count = 0
    while not is_connected():
        if timeout_count == 10:
            log_failure()
        timeout_count += 1
        time.sleep(1000)

    current_instance = Config('config.ini')
    current_instance.read_in()

    # The message consists of the time and date and the name of the pc logged into
    # Feel free to change it as your need fits
    message = ''.join(['Subject: Log in to %s \n\n'
                       'Time logged in: ' % current_instance.PC_NAME,
                       datetime.datetime.now().strftime("%H:%M:%S, %Y-%m-%d")])

    print(current_instance.HOST)
    print(current_instance.PORT)
    print(current_instance.SENDER_ADDRESS)
    print(current_instance.SENDER_PASSWORD)
    print(current_instance.RECEIVER_ADDRESS)
    try:
        server = smtplib.SMTP_SSL(current_instance.HOST, current_instance.PORT)
    except:
        print("Error : Failed to establish connection to the SMTP. Check the host and port is correct")
        exit()
    try:
        server.login(current_instance.SENDER_ADDRESS, current_instance.SENDER_PASSWORD)
    except:
        print(
            "Error : Failed to log in with given credential. Please make sure SMTP_SSL connection is allowed on your "
            "email account.")
        exit()
    try:
        server.sendmail(current_instance.SENDER_ADDRESS, current_instance.RECEIVER_ADDRESS, message)
    except:
        print('Error : Something went wrong in the process of sending a message. Please try again')
        exit()
    server.quit()
    print(message)


if __name__ == '__main__':
    main()
