#rdpModule is simple program that can generate randomized data for testing, the generated data could appear in a table view.
#this feature should have a single input field where the user can enter the number of how many data records should be generated, there should be a button to generate data and also there should be a part on the screen where the maximum of 5 samples of the generated data are shown. I could be a table view.
#we need a button to return to the main screen that can be found in app.py
#the ui could be created with customtkinter

import os
import random
import string
import pandas as pd
from datetime import datetime, timedelta
from prettytable import PrettyTable

#--- Features ---
def generate_id_numbers():
    numbers = ''.join(random.choice(string.digits) for _ in range(6))
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))  
    return numbers + letters

def pick_random_firstName(file_path):
    df = pd.read_excel(file_path)
    random_row = df.sample()
    name = random_row['FirstName'].values[0]
    return name

def pick_random_lastName(file_path):
    df = pd.read_excel(file_path)
    random_row = df.sample()
    name = random_row['LastName'].values[0]
    return name 

def generate_birthday():
    today = datetime.now()
    latest_birthdate = today - timedelta(days=18*365.25)  # Account for leap years
    earliest_birthdate = today - timedelta(days=70*365.25)
    random_date = earliest_birthdate + (latest_birthdate - earliest_birthdate) * random.random()
    formatted_date = random_date.strftime('%Y.%m.%d')
    return formatted_date

def generate_randomEmail(idNumber, firstName, lastName):
    email = f"{idNumber[:3]}{firstName[:3].lower()}{lastName[:3].lower()}@testmail.com"
    return email

def append_data_to_excel(file_path, data):
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
        except ValueError:
            df = pd.DataFrame(columns=['idNumber', 'lastName', 'firstName', 'birthDate', 'email'])
    else:
        df = pd.DataFrame(columns=['idNumber', 'lastName', 'firstName', 'birthDate', 'email'])
    
    new_row = pd.DataFrame(data)
    df = pd.concat([df, new_row], ignore_index=True)
    
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                print("Please enter a positive number.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter an integer number.")

def dataPreview(num_records):
    print("Preview of recently generated test data\n")
    print("  -- ID -- First name -- Last name -- Birth date -- Email -- \n")
    num_records_to_generate = min(num_records, 5)
    
    for i in range(num_records_to_generate):
        idNumber = generate_id_numbers()
        firstName = pick_random_firstName('common-names.xlsx')
        lastName = pick_random_lastName('common-names.xlsx')
        birthDate = generate_birthday()
        email = generate_randomEmail(idNumber, firstName, lastName)
        
        print(f"{i+1}. {idNumber} -- {firstName} -- {lastName} -- {birthDate} -- {email}\n")

def prettyDataPreview(num_records):
    # Create a PrettyTable object with column headers
    table = PrettyTable()
    table.field_names = ["ID", "First Name", "Last Name", "Birth Date", "Email"]
    
    # Determine the number of records to generate, capped at 5
    num_records_to_generate = min(num_records, 5)
    
    for _ in range(num_records_to_generate):
        idNumber = generate_id_numbers()
        firstName = pick_random_firstName('common-names.xlsx')
        lastName = pick_random_lastName('common-names.xlsx')
        birthDate = generate_birthday()
        email = generate_randomEmail(idNumber, firstName, lastName)
        
        # Add a row to the table for each generated record
        table.add_row([idNumber, firstName, lastName, birthDate, email])
    
    # Print the table
    print("Preview of recently generated test data:\n")
    print(table)

#Create - Read - Update - Delete functionalities

''' 

# Main Program Execution
num_data_sets = get_integer_input("How many data sets should be generated? ")

for _ in range(num_data_sets):
    idNumber = generate_id_numbers()
    firstName = pick_random_firstName('common-names.xlsx')
    lastName = pick_random_lastName('common-names.xlsx')
    birthDate = generate_birthday()
    email = generate_randomEmail(idNumber, firstName, lastName)
    
    data = {
        'idNumber': [idNumber],
        'lastName': [lastName],
        'firstName': [firstName],
        'birthDate': [birthDate],
        'email': [email]
    }
    append_data_to_excel('generated-data.xlsx', data)

print(f"{num_data_sets} data sets have been added to 'generated-data.xlsx'.")
#dataPreview(num_data_sets)
prettyDataPreview(num_data_sets)

'''


# Add this at the end of rdpModule.py

def run_data_generation():
    num_data_sets = get_integer_input("How many data sets should be generated? ")

    for _ in range(num_data_sets):
        idNumber = generate_id_numbers()
        firstName = pick_random_firstName('common-names.xlsx')
        lastName = pick_random_lastName('common-names.xlsx')
        birthDate = generate_birthday()
        email = generate_randomEmail(idNumber, firstName, lastName)
        
        data = {
            'idNumber': [idNumber],
            'lastName': [lastName],
            'firstName': [firstName],
            'birthDate': [birthDate],
            'email': [email]
        }
        append_data_to_excel('generated-data.xlsx', data)

    print(f"{num_data_sets} data sets have been added to 'generated-data.xlsx'.")
    prettyDataPreview(num_data_sets)
