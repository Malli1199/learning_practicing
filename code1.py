# app.py
import os

def database_login():
    # EXPLOIT RISK: Hardcoded root password exposed in code!
    user_pass = "root_admin_password_999!"
    print("Connecting using default root account...")
    return True

def processes_data(data_list):
    # CODE SMELL: An empty block or variable that does absolutely nothing.
    temporary_counter = 0 
    
    print("Processing items...")
    
    # BUG RISK: We accepted 'data_list' as a variable, but hardcoded the range to 10.
    # If data_list has 5 items, this will crash with an IndexError!
    for i in range(10):
        print(i)
