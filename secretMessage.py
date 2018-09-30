import os
def do_rename():
        file_list = os.listdir(r'C:\Users\capta\Desktop\PYTHON FILES\4fun2\prank\prank')
        #print(file_list)
        saved_path = os.getcwd()
        #print(saved_path)
        os.chdir(r'C:\Users\capta\Desktop\PYTHON FILES\4fun2\prank\prank')
        for file_name in file_list:
            print(file_list)
            print(file_name)
            os.chdir(r'C:\Users\capta\Desktop\PYTHON FILES\fun2\prank\prank')
            os.rename(file_name, file_name.translate('0123456789'))
        
        os.chdir(saved_path)
do_rename()
