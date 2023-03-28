from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import filedialog
from tkinter import *
import os

root = Tk()
root.withdraw()

#google authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#choosing path
path = filedialog.askdirectory(title='Choose folder to Backup')

folder = os.path.split(path)
folderName=folder[1]

print("Path: ",path)
print("Folder: ",folderName)


numberOfFiles=0
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print("    ",entry)  #list of files in directory
        numberOfFiles+=1

print("Number of files: ",numberOfFiles)

#crating a folder with the same name as choosen one
folder_metadata = {'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'}
folder = drive.CreateFile(folder_metadata)
folder.Upload()
folderID=folder['id']

#uploading files to drive
dir = os.listdir(path)
for file in dir:
    print("    Uploading: ",file)
    File = drive.CreateFile({'title': file,'parents': [{'id': folderID}]})
    File.SetContentFile(path+ "\\" + file)
    File.Upload()



