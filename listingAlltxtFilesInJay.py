import os
import time
a = time.time()
def getAllFilesInDir(*dir):
    fileList = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isfile(dir):
            fileList.append(dir)
    return fileList

def getAllDirsInDir(*dir):
    dirList = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isdir(dir):
            dirList.append(dir)
    return dirList

def joinFileToPath(pathName, fileName):
    return os.path.join(pathName, fileName)

def checkIfFileIs_txt(fileName):
    if fileName.endswith(".txt"):
        return True
    return False

def getAll_txtFilesInFileList(fileList):
    txtFileList = []
    for file in fileList:
        if checkIfFileIs_txt(file):
            txtFileList.append(file)
    return txtFileList

def getNameOFDirInDir(mainDirName, dirToEnterName):
    return mainDirName + "\\" + dirToEnterName

def enterDirInDir(dirToEnter):
    os.chdir(dirToEnter)

def getAll_txtFilesInDir(mainDirName, *dir):
    enterDirInDir(mainDirName)
    fileList = getAllFilesInDir(*dir)
    txtFileList = getAll_txtFilesInFileList(fileList)
    dirList = getAllDirsInDir(*dir)
    for aDir in dirList:
        aDirName = getNameOFDirInDir(mainDirName, aDir)
        txtFileList.append(getAll_txtFilesInDir(aDirName))
    return txtFileList

def getAll_txtFilesInJay():
    JAYPath = "C:\\Users\MR APIRIALA\Desktop\Jay"
    txtFiles = getAll_txtFilesInDir(JAYPath)
    return makeStringFromListOfLists(txtFiles).split(" ")

def makeStringFromListOfLists(listOfLists):
    finalString = ""
    for item in listOfLists:
        if type(item) is type([]):
            finalString += makeStringFromListOfLists(item)
        else:
            finalString += " " + item
    return finalString

if __name__ == "__main__":
    for txtFile in getAll_txtFilesInJay():
        if txtFile != "":
            print(txtFile)
