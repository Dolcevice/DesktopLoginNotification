# DesktopLoginNotification

### TODO : Add task scheduler function for setup []
### TODO : Compile win executables and create release []
### TODO : Write set up guide [x]
### TOdO : Support Unix []

This is a simple, DIY Python script that sends an email when triggered. 
The setup combines the script with the Windows Task Scheduler to run when device is unlocked.

## Set up Guide
1. EXTREMELY RECOMMENDED - Create a google account for sending the message
  - For this program, we are going to need an email address that will serve as the sender of the alerts. <br>
  Making a google account is the best option for this purpose as the host and port is already preconfigured for gmail accounts in the setup process. <br>
  Once you finish making a sender gmail acccount, refer to this guide https://support.google.com/accounts/answer/6010255?hl=en <br>
  and allow 'Less secure apps' which will allow the script to log in and send emails. <br>
  
2. Run the setup.exe
  - When you run the setup program, make sure it is in the same folder as the script.exe and test.exe(if you want to test it). <br>
  Once you see that the config.ini has been created in the same directory, attempt to lock and unlock your device to see the script was successfully scheduled to run. If it sends an email or sms successfully, it is now good to go. 

## Troubleshooting
### TODO : Write this when I finish making a test program.


