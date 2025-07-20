#!/usr/bin/env python3

import subprocess

try:
    result = subprocess.run(["ls", "-l", "/var/log"], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Task unsuccessfull. {result.stderr}")
except FileNotFoundError:
    print("Diredtory not found")
except PermissionError:
    print("Permission to file denied")

"""
This script will always return the FileNotFoundEroor because in windows there's no ls function
Linux and MacOs do have them.
To solve this problem we'd need to import the platform and set it for windows or 
work with WSL and set it up before runing the script through the WSL.
"""

