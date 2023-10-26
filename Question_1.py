#!/usr/bin/env python
# coding: utf-8

# In[10]:


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
        print(f"\nFetching data...\nSuccessfully loaded the {file_location}pandas dataset.")
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
loaded_data_pd= load_pd_file()


# In[22]:


def get_oem_id_details(loaded_data):
        while True:
            try:
                oem_id = input("Enter the oem id: ")

                # Create a flag to check if the OEM ID is found
                oem_id_found = False

                # Initialize a dictionary to store the details
                oem_details = {}

                # Loop through each row in the CSV file
                for row in loaded_data:
                    if row and row[0] == oem_id:
                        # If the OEM ID is found, store the details in the dictionary
                        oem_details["OEM ID"] = oem_id
                        oem_details["Model"] = row[2]
                        oem_details["Manufacturer"] = row[6]
                        oem_details["Weight"] = row[14]
                        oem_details["Price"] = row[15]
                        oem_details["Price Unit"] = row[16]

                        oem_id_found = True
                        break  # Exit the loop as we found the ID

                if not oem_id_found:
                    print("No match for the OEM ID details found.")
                    return None  # Return None if no match is found

                # Print the OEM ID before "OEM ID Details"
                print(f"{oem_id} OEM ID Details:")

                return oem_details  # Return the details as a dictionary
            except ValueError:
                    print("Invalid input. Please enter an integer.")

# Example of how to use the function and retrieve the details
# details = get_oem_id_details(loaded_data)
# if details:
#     for key, value in details.items():
#         print(f"{key}: {value}")


# In[23]:


# def get_oem_id_details(loaded_data):
#     while True:
#         try:
#             oem_id = input("Enter the OEM ID: ").strip()  # Trim leading/trailing whitespaces

#             # Create a flag to check if the OEM ID is found
#             oem_id_found = False

#             # Loop through each row in the loaded data
#             for row in loaded_data:
#                 if row and row[0].strip() == oem_id:  # Trim leading/trailing whitespaces in row[0]
#                     # If the OEM ID is found, print the details
#                     print(f"OEM ID: {oem_id}")
#                     print(f"Model: {row[2]}")
#                     print(f"Manufacturer: {row[6]}")
#                     print(f"Weight: {row[14]}")
#                     print(f"Price: {row[15]}")
#                     print(f"Price Unit: {row[16]}")

#                     oem_id_found = True
#                     break  # Exit the loop as we found the ID
#             break

#             if not oem_id_found:
#                 print("No match for the OEM ID details found.")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
# get_oem_id_details(loaded_data)


# In[25]:


def get_code_name_details(loaded_data):
     #Open the CSV file for reading
    # file_location = "device_features.csv"
    # with open(file_location, "r") as file:
    #     data = csv.reader(file)
        while True:
            try:
                result_rows = []
                code_name = input("Enter the code name: ")

                # Create a flag to check if the code name is found
                code_name_found = False

                # Loop through each row in the CSV file
                for row in loaded_data:
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
                    # Break out of the while loop after displaying the results
                    break
            except ValueError:
                print("Invalid input. Please enter a valid code name (string).")

# call the function
# get_code_name_details(loaded_data)


# In[26]:


def get_ram_capacity_details(loaded_data):
    # # Open the CSV file for reading
    # file_location = "device_features.csv"
    # with open(file_location, "r") as file:
    #     data = csv.reader(file)
        while True:
            try:
                result_rows = []
                ram_size = input("Enter the RAM size: ")  # Add error handling for non-integer input if needed

                # Create a flag to check if the RAM size is found
                ram_size_found = False

                # Loop through each row in the CSV file
                for row in loaded_data:
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
                    # Break out of the while loop after displaying the results
                    break
            except ValueError:
                print("Invalid input. Please enter a valid code name (string).")
# get_ram_capacity_details(loaded_data)


# In[ ]:




# from Question_3 import ram_type_proportion