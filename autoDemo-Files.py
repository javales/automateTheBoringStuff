#! /usr/bin/env python3

##############################################################################
# https://www.udemy.com/course/automate/learn/lecture/3465848?start=0#overview
## Section 11: Files (Lesson 30-34)

### Lesson 30. Filenames and Absolute/Relative File Paths
#########################################################

#Import the os module
import os

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