# Slide 101.
# Process Log Messages


# Task one.

log_message = "ERROR: Unable to connect to database"
normalized_log_message = log_message.lower()
starts_with_error = normalized_log_message.startswith("error")
database_position = normalized_log_message.find("database")
print(f"The normalized version of the message is: {normalized_log_message}")
print(f"The message strats with 'error'?: {starts_with_error}")
print(f"The index for the word database is number {database_position}.")

# Task two.

cpu_usage = 87.6589
rounded_cpu = round(cpu_usage, 2)
remaining_cpu_cap = 100.0 - rounded_cpu
positive_capacity = abs(remaining_cpu_cap) #abs() always returns a positive value.

print(f"Rounded CPU usage: {rounded_cpu}%")
print(f"Remaining cap: {positive_capacity:.2f}%")

# Task three.

user_input = "8080"
is_valid = user_input.isdigit()

print(f"Input valid: {is_valid}")

if is_valid:
    port_number = int(user_input)
    port_squared = pow(port_number, 2)
    print(f"Port squared: {port_squared}")
else:
    print("Invalid input")
