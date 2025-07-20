import os

error_count = 0
print("Current directory:", os.getcwd())
os.chdir(os.path.dirname(__file__))

try:
    with open("server.log", "r") as logfile:
        for line in logfile:
            cleanline = line.strip()
            print(cleanline)

            if "ERROR" in cleanline:
                error_count += 1
                # print(f"Number of errors found: {error_count}")

except FileNotFoundError:
    print(f"The log file was not found. Please check file name")
else:
    print(f"Number of errors found: {error_count}")