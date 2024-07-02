import shutil
import os

# path to source directory
src_dir = input("Enter the source directory in which you want to copy :")
try :
    files = os.listdir(src_dir)
    dest_dir = input("Enter the folder name of copied one")
    shutil.copytree(src_dir, dest_dir)
except FileNotFoundError:
    print("The file is incorrect")
    
    

 

