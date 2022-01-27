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

"""returns, as a string, the name of a directory in the current directory"""
def get_name_of_dir_in_dir(main_dir_name, dir_to_enter_name):
    return main_dir_name + "\\" + dir_to_enter_name

"""enters the directory dirToEnter""" 
def enter_dir_in_dir(dir_to_enter):
    os.chdir(dir_to_enter)
    
"""returns a list of all the .txt files in a list of directories dir
this function uses recursion to access inner directories in directories"""
def get_all_TXT_files_in_dir(main_dir_name, *dir):
    enter_dir_in_dir(main_dir_name)
    file_list = get_all_files_in_dir(*dir)
    txt_file_list = get_all_TXT_files_in_file_list(file_list)
    dir_list = get_all_dirs_in_dir(*dir)
    for a_dir in dir_list:
        a_dir_name = get_name_of_dir_in_dir(main_dir_name, a_dir)
        txt_file_list.append(get_all_TXT_files_in_dir(a_dir_name)) # recursion
    return txt_file_list

"""returns a list of all the .txt files in the Desktop"""
def get_all_TXT_files_in_JAY(user_name):
    JAY_path = f"C:\\Users\{user_name}\Desktop" # you can edit this file path to specify which directory you want to start from
    txt_files = get_all_TXT_files_in_dir(JAY_path)
    return make_string_from_list_of_lists(txt_files).split(" ")

"""returns a string that contains the elements of listOfLists separated by a single space
this function uses recursion to access inner lists in lists"""
def make_string_from_list_of_lists(list_of_lists):
    final_string = ""
    for item in list_of_lists:
        if type(item) is type([]):
            final_string += make_string_from_list_of_lists(item) # recursion
        else:
            final_string += " " + item
    return final_string

if __name__ == "__main__":
    user_name = input("Enter your PC's UserName: ")
    for txt_file in get_all_TXT_files_in_JAY(user_name):
        if txt_file != "":
            print(txt_file)
            
# challenge: after going through the code, copy, paste and edit it in your python ide to be able to retrieve any type of file from a specific directory on your PC :)
