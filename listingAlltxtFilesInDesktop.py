# the code below will output all the .txt files on your desktop
# copy, paste and run it in your python ide to see what it does

import os #importing python os module

# returns a list of all files in directories passed to function as arguments
def getAllFilesInDir(*dir):
    fileList = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isfile(dir):
            fileList.append(dir)
    return fileList

# returns a list of all directories in directories passed to function as arguments
def getAllDirsInDir(*dir):
    dirList = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isdir(dir):
            dirList.append(dir)
    return dirList

# returns a string that contains the filePath to a file
def joinFileToPath(pathName, fileName):
    return os.path.join(pathName, fileName)

# returns boolean to know if the file passed as an argument is a .txt file or not
def checkIfFileIs_txt(fileName):
    return fileName.endswith(".txt"):

# returns a list of all .txt files in the fileList passed to the function as an argument
def getAll_txtFilesInFileList(fileList):
    txtFileList = []
    for file in fileList:
        if checkIfFileIs_txt(file):
            txtFileList.append(file)
    return txtFileList

# returns, as a string, the name of a directory in the current directory
def getNameOFDirInDir(mainDirName, dirToEnterName):
    return mainDirName + "\\" + dirToEnterName

# enters the directory dirToEnter
def enterDirInDir(dirToEnter):
    os.chdir(dirToEnter)
    
# returns a list of all the .txt files in a list of directories dir
# this function uses recursion to access inner directories in directories
def getAll_txtFilesInDir(mainDirName, *dir):
    enterDirInDir(mainDirName)
    fileList = getAllFilesInDir(*dir)
    txtFileList = getAll_txtFilesInFileList(fileList)
    dirList = getAllDirsInDir(*dir)
    for aDir in dirList:
        aDirName = getNameOFDirInDir(mainDirName, aDir)
        txtFileList.append(getAll_txtFilesInDir(aDirName)) # recursion
    return txtFileList

# returns a list of all the .txt files in the Desktop
def getAll_txtFilesInJay(userName):
    JAYPath = f"C:\\Users\{userName}\Desktop" # you can edit this file path to specify which directory you want to start from
    txtFiles = getAll_txtFilesInDir(JAYPath)
    return makeStringFromListOfLists(txtFiles).split(" ")

# returns a string that contains the elements of listOfLists separated by a single space
# this function uses recursion to access inner lists in lists
def makeStringFromListOfLists(listOfLists):
    finalString = ""
    for item in listOfLists:
        if type(item) is type([]):
            finalString += makeStringFromListOfLists(item) # recursion
        else:
            finalString += " " + item
    return finalString

if __name__ == "__main__":
    userName = input("Enter your PC's UserName: ")
    for txtFile in getAll_txtFilesInJay(userName):
        if txtFile != "":
            print(txtFile)
            
# challenge: after going through the code, copy, paste and edit it in your python ide to be able to retrieve any type of file from a specific directory on your PC :)
