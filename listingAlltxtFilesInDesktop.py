"""
the code below will output all the .txt files on your desktop
copy, paste and run it in your python ide to see what it does 
"""

#importing python os module
import os 

"""returns a list of all files in directories passed to function as arguments"""
def get_all_files_in_dir(*dir):
    file_list = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isfile(dir):
            file_list.append(dir)
    return file_list

"""returns a list of all directories in directories passed to function as arguments"""
def get_all_dirs_in_dir(*dir):
    dir_list = []
    dirs = os.listdir(*dir)
    for dir in dirs:
        if os.path.isdir(dir):
            dir_list.append(dir)
    return dir_list

"""returns a string that contains the filePath to a file"""
def join_file_to_path(path_name, file_name):
    return os.path.join(path_name, file_name)

"""returns boolean to know if the file passed as an argument is a .txt file or not"""
def check_if_file_is_TXT(file_name):
    return file_name.endswith(".txt")

"""returns a list of all .txt files in the fileList passed to the function as an argument"""
def get_all_TXT_files_in_file_list(file_list):
    txt_file_list = []
    for file in file_list:
        if check_if_file_is_TXT(file):
            txt_file_list.append(file)
    return txt_file_list

# returns, as a string, the name of a directory in the current directory
def getNameOFDirInDir(mainDirName, dirToEnterName):
    return mainDirName + "\\" + dirToEnterName

# enters the directory dirToEnter
def enterDirInDir(dirToEnter):
    os.chdir(dirToEnter)
    
# returns a list of all the .txt files in a list of directories dir
# this function uses recursion to access inner directories in directories
def getAllTXTFilesInDir(mainDirName, *dir):
    enterDirInDir(mainDirName)
    fileList = getAllFilesInDir(*dir)
    txtFileList = getAllTXTFilesInFileList(fileList)
    dirList = getAllDirsInDir(*dir)
    for aDir in dirList:
        aDirName = getNameOFDirInDir(mainDirName, aDir)
        txtFileList.append(getAllTXTFilesInDir(aDirName)) # recursion
    return txtFileList

# returns a list of all the .txt files in the Desktop
def getAllTXTFilesInJay(userName):
    JAYPath = f"C:\\Users\{userName}\Desktop" # you can edit this file path to specify which directory you want to start from
    txtFiles = getAllTXTFilesInDir(JAYPath)
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
    for txtFile in getAllTXTFilesInJay(userName):
        if txtFile != "":
            print(txtFile)
            
# challenge: after going through the code, copy, paste and edit it in your python ide to be able to retrieve any type of file from a specific directory on your PC :)
