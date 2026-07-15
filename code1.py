# app.py
import os
import sys
import math # ISSUE 1: Unused import (Code Smell)

# ISSUE 2: Hardcoded Secret Key (Critical Security Vulnerability)
API_SECRET_KEY = "AIzaSyD-unsecured-google-api-key-12345"

def process_user_data(user_input):
    # ISSUE 3: Insecure use of eval() on raw user input (Severe Security Vulnerability)
    # A user could pass "os.system('rm -rf /')" and compromise the system!
    result = eval(user_input)
    print("Result of evaluation:", result)

def calculate_average(numbers_list):
    # ISSUE 4: Unused local variable (Code Smell)
    temp_multiplier = 1.5
    
    # ISSUE 5: Potential Division by Zero Bug (Runtime Bug)
    # If the list is empty, len(numbers_list) is 0, causing a crash!
    total_sum = sum(numbers_list)
    average = total_sum / len(numbers_list)
    return average

def add_user_to_list(username, user_list=[]):
    # ISSUE 6: Mutable default argument (Common Python Logic Bug)
    # The default list is created ONCE. Subsequent calls will append to the SAME list!
    user_list.append(username)
    return user_list

def perform_system_cleanup():
    # ISSUE 7: Empty function with just pass (Code Smell / Technical Debt)
    pass

def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        # ISSUE 8: Unreachable Code (Code Smell)
        # Since 'return' happens right above, this line will never run!
        print("This statement is completely useless.")

# --- Code Execution ---
print("Starting execution of questionable code...")
my_users = add_user_to_list("Alice")
print("My Users:", my_users)

other_users = add_user_to_list("Bob") 
# Since user_list is mutable, Bob will unexpectedly have Alice in his list!
print("Other Users (Bug representation):", other_users)