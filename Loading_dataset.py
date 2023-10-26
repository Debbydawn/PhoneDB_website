#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
#"device_features.csv"
file_location = input("Enter the file location: ")
def load_csv_file():
    try:
         #input("Enter file location: ")
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
# call the function
loaded_data = load_csv_file()
# print(loaded_data)


# In[2]:


import pandas as pd

def load_pd_file():
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

# call the function
loaded_data_pd = load_pd_file()


# In[ ]:




