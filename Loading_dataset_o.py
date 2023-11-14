#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# reading in the csv data from csv file using csv  


import csv

file_location = None  # Initialize the variable

def load_csv_file():
    global file_location  # Use the global variable
    while True:
        file_location = input("Enter the file location: ")

        try:
            phone_data = []
            with open(file_location, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for line in reader:
                    phone_data.append(line)
            print(f"\nFetching data...\nSuccessfully loaded the {file_location} dataset.")
            return phone_data

        except csv.Error:
            print(f"Invalid CSV file: {file_location}")
        except FileNotFoundError:
            print(f"File not found: {file_location}")
        except IOError:
            print(f"Couldn't read {file_location}.")

        retry = input("Do you want to enter a new file location? (yes/no): ")
        if retry.lower() != 'yes':
            print("Exiting file loading...\n")
            return None  

# reading in the csv data as a pandas file using pandas        
        
import pandas as pd

def load_pd_file():
    global file_location  # Use the global variable
    if file_location is not None:
        try:
            phone_data = pd.read_csv(file_location, encoding='utf-8')
            print(f"\nFetching data...\nSuccessfully loaded the {file_location} pandas dataset.")
            return phone_data
        except pd.errors.EmptyDataError:
            print(f"Empty CSV file: {file_location}")
        except FileNotFoundError:
            print(f"File not found: {file_location}")
        except pd.errors.ParserError:
            print(f"Couldn't read {file_location}. It may not be a valid CSV file.")
        except Exception as e:
            print(f"An error occurred while loading the file: {str(e)}")

