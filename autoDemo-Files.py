#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 11: Files (Lesson 30-34)

### Lesson 30. Filenames and Absolute/Relative File Paths
#########################################################

#Import the os module
import os
#import shutil below
#import send2trash below

#Joining folders to create a path appropriate to the OS
pathToFile = os.path.join('folder1','folder2','folder3','file.png')
print('Path to file:')
print(pathToFile)
print('')

#the separator/value the join modules uses to join the strings is in the sep variable in os module
print('Separator used by OS:')
print(os.sep)
print('')

#Current Working Directory displayed using os.getcwd() function
print('Current working directory per os.getcwd():')
print(os.getcwd())
print('')

#Change current working directory using os.chdir()
os.chdir('/Proj/study/udemy/automateTheBoringStuff/filesDemo')
print('Current working directory changed with os.chdir():')
print(os.getcwd())
print('')

#Two kinds of file paths: Relative and Absolute

#Absolute - always begins in root folder
#os.path.abspath(pass_in_path_here)
#os.path.isabs(pass in path here) to test Is Absolute Path?
absPath = os.path.abspath('filesDemo')
print('What is the absolute path to this?')
print(absPath)
print('')

absPathCheck = os.path.isabs('filesDemo')
print('Is this an absolute path?')
print(absPathCheck)
print('')

#Relative - relative to current working directory
#. means this directory
#.. means the parent directory
#os.path.relpath() give relative path between two given paths

relaPath = os.path.relpath ('/Proj/study/udemy/automateTheBoringStuff/filesDemo','/Proj')
print('Relative path to filesDemo from Proj:')
print(relaPath)
print('')

#Can capture portions of a path's string value using:
#os.path.dirname()
#os.path.basename()

direPath = os.path.dirname('/Proj/study/udemy/automateTheBoringStuff/filesDemo/filesDemoFile.txt')
print('Path to filesDemoFile.txt per os.path.dirname:')
print(direPath)
print('')

baseName = os.path.basename('/Proj/study/udemy/automateTheBoringStuff/filesDemo/filesDemoFile.txt')
print('Basename of filesDemoFile.txt\'s absolute path per os.path.basename:')
print(baseName)
print('')

baseName = os.path.basename('/Proj/study/udemy/automateTheBoringStuff/filesDemo')
print('Basename of filesDemoFile.txt\'s parent\'s path per os.path.basename:')
print(baseName)
print('')

#Check for existence
#os.path.exists()
iExist = os.path.exists('/Proj/study/udemy/automateTheBoringStuff/filesDemo')
notExist = os.path.exists('/NoPath/study/udemy/automateTheBoringStuff/filesDemo')
print('Since this path DOES exist:')
print(iExist)
print('')

print('Since this path does NOT exist:')
print(notExist)
print('')

#Check if file or folder
#os.path.isfile()
#os.path.isdir()
isFile = os.path.isfile('/Proj/study/udemy/automateTheBoringStuff/filesDemo/filesDemoFile.txt')
isFolder = os.path.isdir('/Proj/study/udemy/automateTheBoringStuff/filesDemo')
print('Since this IS a file:')
print(isFile)
print('')

print('Since this IS a folder:')
print(isFolder)
print('')

#Get size in bytes as integer
#os.path.getsize()
fileSize = os.path.getsize('/Proj/study/udemy/automateTheBoringStuff/filesDemo/filesDemoFile.txt')
print('The File Size is:')
print(fileSize)
print('')

#List dir contents
#os.listdir() NOTICE NOT IN OS.PATH
dirContents = os.listdir('/Proj/study/udemy/automateTheBoringStuff/')
print('Contents of Python study folder:')
print(dirContents)
print('')

#Make new folders use
#os.makedirs() and specify as many folders along a path as needed
#os.makedirs('/1/2/3/4/folders deep')

#Quick program chunk to get size of all files and folders in automateTheBoringStuff

totalSize = 0
for contents in os.listdir('/Proj/study/udemy/automateTheBoringStuff'):
    if not os.path.isfile(os.path.join('/Proj/study/udemy/automateTheBoringStuff', contents)):
        continue
    totalSize = totalSize + os.path.isfile(os.path.join('/Proj/study/udemy/automateTheBoringStuff', contents))
print('Total size of everything in /Proj/study/udemy/automateTheBoringStuff')
print(totalSize)
print('')

### Lesson 30. Filenames and Absolute/Relative File Paths
#   ENDS HERE
#########################################################


print('#########################################################')
print('### Lesson 31. Reading and Writing Plaintext Files')
print('#   STARTS HERE')
print('')

openMyFile = open('/Proj/study/udemy/automateTheBoringStuff/openThis.txt', 'r')

print('Contents of openThis.txt as single string:')
contentsopenMyFile = openMyFile.read()
print('++File Begin++')
print(contentsopenMyFile)
print('--File End--')
print('')

openMyFile.close()

openMyFile = open('/Proj/study/udemy/automateTheBoringStuff/openThis.txt', 'r')

print('Return contents as a list of strings:')
contentsAsList = openMyFile.readlines()
print(contentsAsList)
print('')

openMyFile.close()

#Open file in Write mode with 'w' or 'a' for Append mode
#If file does not already exist, Python will create it
#Write to file with objectName.write() function
openMyFileAppend = open('/Proj/study/udemy/automateTheBoringStuff/openApendToThis.txt', 'a')
openMyFileAppend.write('Hello Squirrels!!!')
openMyFileAppend.write('How\'s the weather?')
openMyFileAppend.close()

openMyFileAppend = open('/Proj/study/udemy/automateTheBoringStuff/openApendToThis.txt', 'r')
print('Return contents of appended file openApendToThis.txt as a list of strings:')
contentsAsList = openMyFileAppend.readlines()
print(contentsAsList)
print('')

openMyFile.close()

#To save complex data structures like lists and dictionaries to binary shelve files
import shelve

shelfFile = shelve.open('myData')
#Save data to shelfFile as if dictionary

#Save to a key called cats
shelfFile['cats'] = ['Zophie','Pooka','Simon']

shelfFile.close()

shelfFile = shelve.open('myData')
print('Contents of myData shelf file created by shelve.open(\'myData\'):')
print(shelfFile['cats'])
print('')

shelfFile.close()

#shelve also has a keys and values method
shelfFile = shelve.open('myData')
shelfKeysAsList = list(shelfFile.keys())
print('Keys of myData shelf file by shelfFile.keys():')
print('Unfiltered:')
print(shelfFile.keys())
print('')
print('As List:')
print(shelfKeysAsList)
print('')

#unlike file open(), didn't have to close, first
shelfValuesAsList = list(shelfFile.values())
print('Values of myData shelf file by shelfFile.values():')
print('Unfiltered:')
print(shelfFile.values())
print('')
print('As List:')
print(shelfValuesAsList)
print('')

shelfFile.close()

print('### Lesson 31. Reading and Writing Plaintext Files')
print('#   ENDS HERE')
print('#########################################################')
print('')

print('#########################################################')
print('### Lesson 32. Copying and Moving Files and Folders')
print('#   STARTS HERE')
print('')

#To access copy()
import shutil

#Copy or Rename a single file
os.chdir('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround')
print('Copying /Proj/study/udemy/automateTheBoringStuff/moveStuffAround/filesDemoFile.txt to FirstFolder')
print('')
shutil.copy('filesDemoFile.txt','/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder')

print('Renaming /Proj/study/udemy/automateTheBoringStuff/moveStuffAround/filesDemoFile.txt to FirstFolder')
print('')
shutil.copy('filesDemoFile.txt','/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/filesDemoFileRenamed.txt')

#Copy a folder and contents (use dirs_exist_ok argument when folder already exists
print('Copy FirstFolder contents to SecondFolder')
print('')
shutil.copytree('FirstFolder','SecondFolder',dirs_exist_ok=True)

#Move or rename a file using shutil.move()

#Ensuring myData file exists by repeating shelve commands
shelfFile = shelve.open('myData')
shelfFile['cats'] = ['Zophie','Pooka','Simon']
shelfFile.close()

print('Move myData.db to SecondFolder and rename it')
print('')
shutil.move('myData.db','SecondFolder/myDataMoved.db')

print('### Lesson 32. Copying and Moving Files and Folders')
print('#   ENDS HERE')
print('#########################################################')
print('')


print('### Lesson 33. Deleting Files')
print('#   STARTS HERE')
print('#########################################################')
print('')
#import os already done above
# os.unlink() to delete files
# os.rmdir()
#import shutil already done above

#Delete the file created by the autoDemo-FilesCreate.py with os.unlink()
#os.unlink('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/deleteThis.txt')

#Delete the empty DeleteThisEmpty folder with os.rmdir()
#print('Delete /Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisEmpty')
#os.rmdir('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisEmpty')
#print('')

#Delete the non-empty DeleteThisTree with shutil.rmtree()
#print('Delete /Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisTree')
#shutil.rmtree('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisTree')
#print('')

#Fail to delete the non-empty DeleteThisFolder
#print('**EXPECTED*** Fail to delete non-empty /Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisFolder')
#os.rmdir('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteThisFolder')
#print('')

#Delete contents of folder with for loop

#Install send2trash with 'pip install send2trash' to send to recycle bin instead of immediate deletion; both files and folders
import send2trash

os.chdir('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteContents')
print('Print cwd:')
print(os.getcwd())
for filename in os.listdir('/Proj/study/udemy/automateTheBoringStuff/moveStuffAround/FirstFolder/AnotherFolder/DeleteHere/DeleteContents'):
    if filename.endswith('.rxt'):
        print('Deleting ' + filename + '!')
        #use send2trash instead of unlink
        send2trash.send2trash(filename)
        #os.unlink(filename)

print('')



print('')

print('### Lesson 33. Deleting Files')
print('#   ENDS HERE')
print('#########################################################')
print('')
