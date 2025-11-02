import os
import platform
import string

def system_info():
    if os.name == "nt":
        available_drives = [f"{d}:" for d in string.ascii_uppercase if os.path.exists(f"{d}:")]
    else:
        available_drives = ["Not supported on this OS"]

    print("Operating System Information:")
    print(f"OS Name: {platform.system()}")
    print(f"Username: {os.getlogin()}")
    print(f"System Directory: {os.path.abspath(os.sep)}")
    print(f"System Directory: {os.environ.get('SYSTEMROOT', 'N/A')}")
    print(f"CPU Count: {os.environ.get("NUMBER_OF_PROCESSORS", "Unknown")}")
    print(f"CPU Count: {os.cpu_count()}")
    print(f"Available Drives: {available_drives}")


system_info()