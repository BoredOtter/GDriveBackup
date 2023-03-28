# GDriveBackup

This Python script allows you to backup a local folders to Google Drive using the PyDrive library. After authenticating your Google Drive account, the script will prompt you to choose the local folder to backup. It will then create a folder with the same name on your Google Drive and upload all files from the local folder to the newly created folder on Google Drive.

**Before using this script, you must:** 
- Set up a Google Drive API or/and Google Console Cloud
- Add Google account as tester for this app in Google API
- Download API keys and add them as **clients_secrets.json** to the same localization as **main.py**



## Requirements

-   PyDrive
-   tkinter
-  Properly setted Google Account and Google API

## Usage

1.  Install the required libraries.
2.  Run the script.
3.  Authenticate your Google Drive account.
4.  Choose the local folder to backup.
5.  The script will automatically create a folder with the same name on your Google Drive and upload all files from the local folder to the newly created folder on Google Drive.
