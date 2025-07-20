# Homework
# Slide 75

# Task one.
server_metrics = {
    "server1": [50, 70],
    "server2": [85, 90],
    "server3": [40, 60],
}

def analyze_server(server_name, metrics):
    if type(metrics) is not list:
        raise ValueError("Metrics must be a list.")
    total_usage = sum(metrics)
    num_metrics = len(metrics)
    average_usage = total_usage / num_metrics
    return average_usage

# Task two.

def check_overutilized(servers, threshold=80):
    overutilized = []
    for server, metrics in servers.items():
        avg_usage = analyze_server(server, metrics)
        if avg_usage > threshold:
            overutilized.append(server)
    return overutilized

# Task three.

def generate_report(servers):
    total_cpu = 0
    total_mem = 0
    server_count = len(servers)
    for metrics in servers.values():
        total_cpu += metrics[0]
        total_mem += metrics [1]
    print(f"Number of Servers monitored: {server_count}")
    print(f"Total CPU usage: {total_cpu}, average CPU usage: {total_cpu / server_count}%")
    print(f"Total RAM usage: {total_mem}, average RAM usage: {total_mem / server_count}%")


# Running script.
print("Analizing Server metrics...\n")
for server, metrics in server_metrics.items():
    analyze_server(server, metrics)

print("Searching for overutilization of resources in each Server...\n")
overutilized_servers = check_overutilized(server_metrics)
if overutilized_servers:
    print("Over-utilized servers:", overutilized_servers)
else:
    print("All Servers running within parameters.")

print("\nGenerating report:\n")
generate_report(server_metrics)
