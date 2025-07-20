# Slide 87
# Setup

servers = ["server1", "server2", "server3"]
active_servers = servers
# Q1: Yes, active_server is a pointer to the allocated ram of servers rather than the content itslef.
# Q2:
print("Servers:", servers)
print("Active servers:", active_servers)
print(f"RAM address of servers is: {id(servers)}, RAM address of active-servers is {id(active_servers)}\n")

# Task two. Managing immutables.

server_ip = "192.162.1.1"
server_endpoint = server_ip + ":80"
# Q1 Because is a str which maskes it immutable. So server_endpoint aquires a new RAM address for the new str.
# Q2:
print(f"Server IP:", {server_ip})
print(f"Server Endpoint:", {server_endpoint})
print(f"server_ip RAM address is {id(server_ip)}")
print(f"server_endpoint RAM address is {id(server_endpoint)}\n")

# Task three. Using mutables.

server_roles = {"server1": "web", "server2": "db", "server3": "cache"}
server_roles["server4"] = "monitoring"
safe_server_roles_copy = server_roles.copy()
all_roles = server_roles
all_roles["server1"] = "proxy"
# server_roles["server5"] = "stand by"

# Q1: Yes, as they both point to the same RAM address, all changes on either will reflect on both.
# Q2: By making a safe copy of server_roles before creating the link between server_roles and all_roles.
#   That way the safe copy has a new RAM address thus is not affected by any modification done in the future. Line 30
print(f"Original server roles:, {server_roles}")
print(f"Modified all roles:, {all_roles}")
print(f"Safe server copy:, {safe_server_roles_copy}\n")

# Task four. Immutable v mutable in a function.

def update_server_list(server):
    server.append("serverX")

server = ["serverA", "serverB"]
safe_server_list_copy = server.copy()
print(f"Servers list: {server}")
update_server_list(server)
print(f"Updated servers list: {server}")

# Q1: In the def I use the server list. So any and all modifications will be stored in the RAM address
#   even if no print is done.
# Q2: Making a copy like in task three

print(f"Original server list, before append: {safe_server_list_copy}\n")

# Bonus round.

def assing_roles(server_list, role):
    new_roles = {}
    for server in server_list:
        new_roles[server] = role
    return new_roles

server_list = ["srv1", "srv2", "srv3"]

print(f"Original servers: {server_list}")
updated_rolls = assing_roles(server_list, "Standing by...")
print(f"New roles assigned list: {updated_rolls}\n")