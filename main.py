import getpass
import support

class FileMal:
    def __init__(self):
        self.F = support.FileMalFunctions()
        self.user_name = getpass.getuser()

    """returns a list of all the .txt files in the Desktop"""

    def get_all_files_in(self, file_type):
        path = f"C:\\Users\{self.user_name}\Desktop"  # you can edit this file path to specify which directory you want to start from
        files = self.F.get_all_such_files_in_dir(path, file_type)
        return self.F.make_string_from_list_of_lists(files).split(" ")
    
# challenge: after going through the code, copy, paste and edit it in your python ide to be able to retrieve any type of file from a specific directory on your PC :)
