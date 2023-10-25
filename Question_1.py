#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[9]:


import csv

def load_csv_file():
    try:
        file_location = "device_features.csv" #input("Enter file location: ")
        airbnb_data = []
        with open(file_location, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                airbnb_data.append(line)
            print(f"\nFetching data...\nSuccessfully loaded the {file_location} dataset.")
            return airbnb_data
    except csv.Error:
        print(f"Invalid CSV file: {file_location}")
    except FileNotFoundError:
        print(f"File not found: {file_location}")
    except IOError:
        print(f"Couldn't read {file_location}.")


# In[10]:


# Open the CSV file and use 'with' to ensure it's properly closed after reading
file_location = "device_features.csv"
with open(file_location, "r") as file:
    data = csv.reader(file)

    oem_id = input("Enter the oem id: ")
    
    # Create a flag to check if the OEM ID is found
    oem_id_found = False

    # Loop through each row in the CSV file
    for row in data:
        if row and row[0] == oem_id:
            # If the OEM ID is found, print the details
            value1 = row[2]
            value2 = row[6]
            value3 = row[14]
            value4 = row[15]
            value5 = row[16]

            print("The OEM ID {} details are:".format(oem_id))
            print("The model of the device is:", value1)
            print("The manufacturer is:", value2)
            print("The weight of the device is:", value3)
            print("The price of the device is:", value4)
            print("The price unit is:", value5)

            oem_id_found = True
            break  # Exit the loop as we found the ID

    if not oem_id_found:
        print("No match for the OEM ID details found.")


# In[21]:


# Open the CSV file for reading
file_location = "device_features.csv"
with open(file_location, "r") as file:
    data = csv.reader(file)
    result_rows = []
    code_name = input("Enter the code name: ")

    # Create a flag to check if the code name is found
    code_name_found = False

    # Loop through each row in the CSV file
    for row in data:
        if row and row[7] == code_name:
            # If the code name is found, create a dictionary with details
            value1 = row[1]
            value2 = row[2]
            value3 = row[23]
            value4 = row[44]
            value5 = row[45]
            row_dict = {
                "Brand": value1,
                "Model name": value2,
                "RAM": value3,
                "Market regions": value4,
                "Date of addition": value5
            }
            result_rows.append(row_dict)

            code_name_found = True

    if not code_name_found:
        print("No match for the code name details found.")
    else:
        num_rows = 20
        start_pos = 0
        end_pos = min(start_pos + num_rows, len(result_rows))

        while True:
            for i in range(start_pos, end_pos):
                row = result_rows[i]
                print("Brand:", row["Brand"])
                print("Model name:", row["Model name"])
                print("RAM:", row["RAM"])
                print("Market region:", row["Market regions"])
                print("Date of addition:", row["Date of addition"])
                print()

            if end_pos >= len(result_rows):
                print("No more rows available.")
                break

            user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
            if user_input == 'next':
                start_pos += num_rows
                end_pos = min(start_pos + num_rows, len(result_rows))
            elif user_input == 'quit':
                print("The display of results is stopping...")
                print("Stopped")
                break


# In[19]:


# Open the CSV file for reading
file_location = "device_features.csv"
with open(file_location, "r") as file:
    data = csv.reader(file)
    result_rows = []
    ram_size = input("Enter the RAM size: ")  # Add error handling for non-integer input if needed

    # Create a flag to check if the RAM size is found
    ram_size_found = False

    # Loop through each row in the CSV file
    for row in data:
        if row and row[23] == ram_size:  
            # If the RAM size is found, create a dictionary with details
            value1 = row[0]
            value2 = row[3]
            value3 = row[4]
            value4 = row[13]
            value5 = row[9]
            row_dict = {
                "OEM Id": value1,
                "Release date": value2,
                "Announcement date": value3,
                "Dimensions": value4,
                "Device category": value5
            }
            result_rows.append(row_dict)

            ram_size_found = True

    if not ram_size_found:
        print("No match for the RAM size details found.")
    else:
        num_rows = 20
        start_pos = 0
        end_pos = min(start_pos + num_rows, len(result_rows))

        while True:
            for i in range(start_pos, end_pos):
                row = result_rows[i]
                print("OEM Id:", row["OEM Id"])
                print("Release date:", row["Release date"])
                print("Announcement date:", row["Announcement date"])
                print("Dimensions:", row["Dimensions"])
                print("Device category:", row["Device category"])
                print()

            if end_pos >= len(result_rows):
                print("No more rows available.")
                break

            user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")
            if user_input == 'next':
                start_pos += num_rows
                end_pos = min(start_pos + num_rows, len(result_rows))
            elif user_input == 'quit':
                print("The display of results is stopping...")
                print("Stopped")
                break


# In[ ]:




