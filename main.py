from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import filedialog
from tkinter import *
import os

root = Tk()
root.withdraw()
#acvalhlalla ID: 1KP9K5aXPOicSUFkd9x97ccnEiwROHvsn

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

#folder_list = drive.ListFile({'q': "trashed=false"}).GetList()

#for folder in folder_list:
#    print ('folder title: %s, id: %s' % (folder['title'], folder['id']))
print("window")


folder_selected = filedialog.askdirectory(title='Choose folder to Backup')
path = folder_selected
print("windo2w")
#path = r"C:\Users\eryks\AppData\Roaming\Goldberg UplayEmu Saves\13504"
print("Path: ",path)


numberOfFiles=0
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        #print(entry)  #list of files in directory
        numberOfFiles+=1

print("Number of files: ",numberOfFiles)

dirs = os.listdir( path )

folder_id = 'parent_folder_id'

folder_metadata = {'title' : 'MyFolder', 'mimeType' : 'application/vnd.google-apps.folder'}
folder = drive.CreateFile(folder_metadata)
folder.Upload()

# This would print all the files and directories

#numberOfFiles = 

# # for file in dirs:
# #    print(file)
# #    file1 = drive.CreateFile({'title': file,'parents': [{'id': '1KP9K5aXPOicSUFkd9x97ccnEiwROHvsn'}]})
# #    file1.SetContentFile(path+ "\\" + file)
# #    file1.Upload()

# # print("Number of files: ",file.__len__())


