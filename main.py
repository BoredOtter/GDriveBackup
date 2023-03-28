from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import filedialog
from tkinter import *
import os



#google authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#choosing path
root = Tk()
root.withdraw()
path = filedialog.askdirectory(title='Choose folder to Backup')

folderName=os.path.split(path)[1]

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
temp = 0
for file in dir:
    temp+=1
    print("    Uploading ",temp,"/",numberOfFiles," : ",file)
    File = drive.CreateFile({'title': file,'parents': [{'id': folderID}]})
    File.SetContentFile(path+ "\\" + file)
    File.Upload()
    
print("Files uploaded!")


