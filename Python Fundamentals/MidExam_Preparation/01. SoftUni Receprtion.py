import math
first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())

total_students = int(input())

employee_capacity = first_employee_capacity+second_employee_capacity+third_employee_capacity

time_needed = total_students/employee_capacity
extra_time = time_needed//3
if time_needed >= 3:
    time_needed += extra_time
print(f"Time needed: {math.ceil(time_needed)}h.")

