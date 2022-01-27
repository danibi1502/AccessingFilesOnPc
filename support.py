import os
import getpass

"""returns a list of all files in directories passed to function as arguments"""

class FileMalFunctions:
    def __init__(self):
        pass

    """returns a list of all files in directories passed to function as arguments"""

    def get_all_files_in_dir(self, *dir):
        file_list = []
        dirs = os.listdir(*dir)
        for dir in dirs:
            if os.path.isfile(dir):
                file_list.append(dir)
        return file_list

    """returns a list of all directories in directories passed to function as arguments"""

    def get_all_dirs_in_dir(self, *dir):
        dir_list = []
        dirs = os.listdir(*dir)
        for dir in dirs:
            if os.path.isdir(dir):
                dir_list.append(dir)
        return dir_list

    """returns a string that contains the filePath to a file"""

    def join_file_to_path(self, path_name, file_name):
        return os.path.join(path_name, file_name)

    """returns boolean to know if the file passed as an argument is a .txt file or not"""

    def check_if_file_is(self, file_name, file_type):
        return file_name.endswith("." + file_type)

    """returns a list of all .txt files in the fileList passed to the function as an argument"""

    def get_all_files_in_file_list(self, file_list, file_type):
        type_file_list = []
        for file in file_list:
            if self.check_if_file_is(file, file_type):
                type_file_list.append(file)
        return type_file_list

    """returns, as a string, the name of a directory in the current directory"""

    def get_name_of_dir_in_dir(self, main_dir_name, dir_to_enter_name):
        return main_dir_name + "\\" + dir_to_enter_name

    """enters the directory dirToEnter"""

    def enter_dir_in_dir(self, dir_to_enter):
        os.chdir(dir_to_enter)

    """returns a list of all the .txt files in a list of directories dir
    this function uses recursion to access inner directories in directories"""

    def get_all_such_files_in_dir(self, main_dir_name, file_type, *dir):
        self.enter_dir_in_dir(main_dir_name)
        file_list = self.get_all_files_in_dir(*dir)
        txt_file_list = self.get_all_files_in_file_list(file_list, file_type)
        dir_list = self.get_all_dirs_in_dir(*dir)
        for a_dir in dir_list:
            a_dir_name = self.get_name_of_dir_in_dir(main_dir_name, a_dir)
            txt_file_list.append(self.get_all_such_files_in_dir(a_dir_name, file_type))  # recursion
        return txt_file_list

    """returns a string that contains the elements of listOfLists separated by a single space
    this function uses recursion to access inner lists in lists"""

    def make_string_from_list_of_lists(self, list_of_lists):
        final_string = ""
        for item in list_of_lists:
            if type(item) is type([]):
                final_string += self.make_string_from_list_of_lists(item)  # recursion
            else:
                final_string += " " + item
        return final_string

