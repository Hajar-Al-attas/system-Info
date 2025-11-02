import os
import platform
import string

nameOS = platform.system()

def disks():
    if nameOS == "Windows":
        return [f"{d}:" for d in string.ascii_uppercase if os.path.exists(f"{d}:")]
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
    available_drives = disks()

    print("Operating System Information:")
    print(f"OS Name: {nameOS}")
    print(f"Username: {os.getlogin()}")
    print(f"System Directory: {system_directory}")
    print(f"CPU Count: {os.cpu_count()}")
    print(f"Available Drives : {available_drives}")


system_info()