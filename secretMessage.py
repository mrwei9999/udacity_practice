import os
def rename():
        file_list = os.listdir(r'C:\Users\capta\Desktop\PYTHON FILES\4fun2\prank\prank')
        saved_path = os.getcwd()
        os.chdir(r'C:\Users\capta\Desktop\PYTHON FILES\4fun2\prank\prank')
        for file_name in file_list:
            os.rename(file_name, file_name.translate('0123456789'))
        os.chdir(saved_path)
rename()
