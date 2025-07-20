# Slide 106
# Task one.

line_count = 0
for _ in range(100):
    line_count += 1

print(f"Line count: {line_count}")

"""
The task was to print one line at the end with the full line count to 100.
Hence no other print was done in the code.
Since I'm not asked to keep a new variable and use it in any form, the use for:
for i in range(100):
the _ in line 5 is python convention for situations like this one.
"""

# Task two.

cpu_usage = 50.0

cpu_usage += 10.0
print(f"Increased CPU usage: {cpu_usage}")

cpu_usage -= 5.0
print(f"Decreased CPU usage: {cpu_usage}")
"""
At first I though of creating a new variable for the base cpu usage. 
But at a second glance at the task asked for, there's no need to reset the cpu usage value after 
each usage change. So the 'updated' value can be carried by the task proposition.
Also, verified by the example output.
"""

# Task three.

log_entries = 245
page_size = 50

full_pages = log_entries
full_pages //= page_size
print(f"Full pages = {full_pages}")
"""
This part, because of the double / sign (line 40) changes the mathematical operation from
a normal division to a 'int' returning calculation. Therefore the answer is a whole number.
"""

remaining_logs = log_entries
remaining_logs %= page_size
print(f"The remaining logs are {remaining_logs}")

"""
In this part the %= retunrs the byproduct of the previous operation. 
The 45 logs that weren't included in the int result of the //= can be found and isolated with the %=
"""
# Task four.

metric = 2
metric **= 3

print(f"Exponential value of metric after math: {metric}")

