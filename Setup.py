import configparser
import os

Success = 0
User_Exit = 1
Config_failure = 2
Not_Win = 3


class ConfigInfo:
    def __init__(self):
        self.sender_address = ''
        self.sender_password = ''
        self.receiver_address = ''
        self.pc_name = ''
        self.host = 'smtp.gmail.com'
        self.port = 465


def print_line():
    print('----------------------------------------------------------')


def generate_configuration(dln_config, sender_address, sender_password, receiver_address, pc_name, host, port):
    dln_config['SENDER'] = {'Address': sender_address,
                            'Password': sender_password,
                            'Host': host,
                            'Port': port}
    dln_config['RECEIVER'] = {'Address': receiver_address}
    dln_config['MISC'] = {'PC_Name': pc_name}

    with open('config.ini', 'w') as config_file:
        dln_config.write(config_file)


def main():
    dln_config = configparser.ConfigParser()
    info = ConfigInfo()

    print('DesktopLoginNotification - Created by Yun Ho Jung')
    print('Original releases from https://github.com/Dolcevice/DesktopLoginNotification')

    if not os.name == 'nt':
        print('This program is intended for Windows and will not work with other operating systems')
        input('Press enter to exit')
        exit(Not_Win)

    print('Enter y|Y to continue with setup. Enter any other key to stop setup')
    confirmation = input()
    if not (confirmation == 'y' or confirmation == 'Y'):
        exit(User_Exit)

    while True:
        print_line()
        print('WARNING : It is highly recommended that you create a gmail account for the purpose of sending.')
        print('The credentials will be STORED IN PLAINTEXT and is not secure whatsoever.')
        print_line()
        # Host and port
        print('Step 1. Host and port of the sender')
        print('Is the sender email address using Gmail? Or, would you like to manually input the host and port?')
        print(
            'Enter y|Y to automatically use host and port for gmail. Enter any other key to manually input '
            'host and port')
        confirmation = input()
        if not (confirmation == 'y' or confirmation == 'Y'):
            while True:
                print('Please enter the host of the sender email: ')
                info.host = input()
                print('%s - is this information correct? Enter y|Y to confirm', info.host)
                confirmation = input()
                if not (confirmation == 'y' or confirmation == 'Y'):
                    continue
                else:
                    break
            while True:
                print('Please enter the port of the sender email: ')
                info.port = input()
                print('%s - is this information correct? Enter y|Y to confirm', info.port)
                confirmation = input()
                if not (confirmation == 'y' or confirmation == 'Y'):
                    continue
                else:
                    break
        print_line()
        # Credentials
        print('Step 2: Email address and password of the sender')
        while True:
            print('Please enter the email address of the sender.')
            print('If Gmail, MAKE SURE LESS SECURE APP ACCESS IS TURNED OFF, otherwise the login does not work.')
            info.sender_address = input()
            print('%s - is this information correct? Enter y|Y to confirm', info.sender_address)
            confirmation = input()
            if not (confirmation == 'y' or confirmation == 'Y'):
                continue
            else:
                break
        while True:
            print('Please enter the password of the sender.')
            print(
                'HIGHLY RECOMMENDED THAT THIS IS NOT YOUR MAIN EMAIL ADDRESS. PASSWORD IS GOING TO BE STORED IN '
                'PLAINTEXT')
            info.sender_password = input()
            print('%s - is this information correct? Enter y|Y to confirm', info.sender_password)
            confirmation = input()
            if not (confirmation == 'y' or confirmation == 'Y'):
                continue
            else:
                break
        print_line()
        # Receiving end
        print('Step 3 : Information of the receiver')
        while True:
            print('Please enter the email address of the receiver.')
            print('If you would like to send a message to a phone, please refer to the README guide.')
            info.receiver_address = input()
            print('%s - is this information correct? Enter y|Y to confirm', info.receiver_address)
            confirmation = input()
            if not (confirmation == 'y' or confirmation == 'Y'):
                continue
            else:
                break

        print_line()
        # Optional - naming
        print('Optional - Step 4 : Information of the unlocked PC')
        print(
            'Would you like to name the pc that is being notified of? This is optional as long as you can keep track '
            'of which pc is being unlocked.')
        confirmation = input()
        if confirmation == 'y' or confirmation == 'Y':
            while True:
                print('Please enter the name of the PC that will be notified of')
                print('If you would like to send a message to a phone, please refer to the README guide.')
                info.pc_name = input()
                print('%s - is this information correct? Enter y|Y to confirm', info.pc_name)
                confirmation = input()
                if not (confirmation == 'y' or confirmation == 'Y'):
                    continue
                else:
                    break
        else:
            pass
        print_line()
        # confirmation
        print('Please review that the given information are correct: ')
        print('Host : %s', info.host)
        print('Port : %s', info.port)
        print('Sender Address : %s', info.sender_address)
        print('Sender Password : %s', info.sender_password)
        print('Receiver Address : %s', info.receiver_address)
        print('PC Name : %s', info.pc_name)

        print('Press any key to continue. If you would like to re-enter the information, enter "REDO"')
        confirmation = input()
        if confirmation == 'REDO':
            continue
        else:
            break
    print('Setting up!')
    try:
        generate_configuration(dln_config, info.sender_address, info.sender_password, info.receiver_address,
                               info.pc_name, info.host, info.port)
    except:
        print('Configuration file could not be generated.')
        input('Press enter to exit')
        exit(Config_failure)
    print('Configuration successfully generated.')
    print('Setup complete! Press enter to exit.')
    exit(Success)


if __name__ == "__main__":
    main()
