# Slide 96

# Task one. Exploring core types.

server_id = 101                     # int
cpu_usage = 75.3                    # float
status_msg = "Server is running"    # string
is_ready = True                     # boolean

print(f"{server_id} is a {type(server_id)} value type.")
print(f"{cpu_usage} is a {type(cpu_usage)} value type.")
print(f"{status_msg} is a {type(status_msg)} value type.")
print(f"{is_ready} is a {type(is_ready)} value type.")

# Task two. Convert and Validate data.
raw_cpu_usage = "85.6"
raw_is_ready = "True"

converted_cpu = float(raw_cpu_usage)
if raw_is_ready == "True":
    converted_ready = True
else:
    converted_ready = False

print("--- Type Conversion ---")
print(f"raw_cpu_usage {raw_cpu_usage} (str) has been converted to: {converted_cpu} that is type {type(converted_cpu)}")
print(f"raw_is_ready {raw_is_ready} (str) has been converted to: {converted_ready} that is type {type(converted_ready)}")
"""
Q: What happens if raw_is_ready is "False" or an empty string?
A: It will convert to False, refer if loop. Anything other than "True" will be a boolean False.
Q: What if cpu data is invalid like "abc"?
A: The app will crash with ValueError.
"""

# Task three. Operations with types.

max_cpu_usage = 100.0
available_cpu = max_cpu_usage - cpu_usage

print(f"The available CPU now is of {available_cpu:.2f}%")

if is_ready and cpu_usage < 90.0:
    print("Server is oeprational")
else:
    print("Server is overloaded or not ready")

# Task four. Handling a list of servers.
servers = [
    {"id": 1, "cpu": 45.0, "status": "running", "ready": True},
    {"id": 2, "cpu": 92.5, "status": "running", "ready": False},
    {"id": 3, "cpu": 78.3, "status": "stopped", "ready": False},
]

for server in servers:          #Grabing values from the list by their name, not index
    serverid = server["id"]
    cpu = server["cpu"]
    ready = server["ready"]

    print(f"Server {serverid} is running at {cpu}%")

    if ready and cpu < 80.0:
        print(f"Server {serverid} is under normal load")
    else:
        print(f"Server {serverid} needs attention")
