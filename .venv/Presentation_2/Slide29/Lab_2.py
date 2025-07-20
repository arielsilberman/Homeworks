#!/usr/bin/env python3

import subprocess

# Use systemctl as per instructions...
check_cmd = ["systemctl", "is-active", "nginx"]

try:
    result = subprocess.run(check_cmd, capture_output=True, text=True)

    if result.returncode == 0 and result.stdout.strip() == "active":
        print("nginx is running.")
    else:
        print("nginx is NOT running. Attempting to restart...")

        restart_cmd = ["sudo", "systemctl", "restart", "nginx"]
        restart_result = subprocess.run(restart_cmd, capture_output=True, text=True)

        if restart_result.returncode == 0:
            print("nginx restarted successfully.")
        else:
            print("Failed to restart nginx.")
            print("stderr:", restart_result.stderr)

except FileNotFoundError:
    print("systemctl not found. Is systemd enabled in your WSL?")
except PermissionError:
    print("Permission denied. Try running this script with sudo.")
except Exception as e:
    print(f"Unexpected error: {e}")