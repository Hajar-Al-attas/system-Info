import os
import platform
import string

nameOS = platform.system()

def drive():
    if nameOS == "Windows":
        return os.listdrives()
    elif nameOS == "Linux" :
        return os.popen("lsblk -d -n -o NAME").read().splitlines()
    elif nameOS == "Darwin":
        return os.popen("diskutil list").read().splitlines()
    else:
        return "UnKnowin OS"
    

def root_path():
    return os.environ.get('SYSTEMROOT',os.path.abspath(os.sep))

            
def system_info():

    system_directory = root_path()
    drives = drive()

    print("Operating System Information:")
    print(f"OS Name: {nameOS}")
    print(f"Username: {os.getlogin()}")
    print(f"System Directory: {system_directory}")
    print(f"CPU Count: {os.cpu_count()}")
    print(f"Drives : {drives}")


system_info()

