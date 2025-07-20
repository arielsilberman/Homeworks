import os
import shutil

print(f"Current directory: {os.getcwd()}")

os.chdir(os.path.dirname(__file__))

og_file = "nginx.conf"
backed_file = "ngingx.conf.bak"

try:
    shutil.copy(og_file, backed_file)
    print(f"Backup successfull, file name: {backed_file}")
except FileNotFoundError:
    print(f"The original file '{og_file}' couldn't be found.")
except PermissionError:
    print(f"Permission to {og_file} denied.")
