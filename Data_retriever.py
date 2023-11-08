# loading dataset
from Loading_dataset import load_csv_file



def get_oem_id_details(loaded_data):
    try:
        oem_id = input("Enter the OEM ID: ").lower()  # Convert input to lowercase

        # Create a flag to check if the OEM ID is found
        oem_id_found = False

        # Initialize a dictionary to store the details
        oem_details = {}

        # Loop through each row in the CSV file
        for row in loaded_data:
            if row and row[0].lower() == oem_id:  # Compare in lowercase
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
    except IndexError:
        print("Index error. Make sure your data has enough columns.")
    except Exception as e:
        print(f"An error occurred: {e}")




def get_code_name_details(loaded_data):
    while True:
        try:
            result_rows = []
            code_name = input("Enter the code name: ").lower()  # Convert input to lowercase

            # Create a flag to check if the code name is found
            code_name_found = False

            # Loop through each row in the CSV data
            for row in loaded_data:
                if row and row[7].lower() == code_name:  # Compare in lowercase
                    # If the code name is found, create a dictionary with details
                    value1 = row[34]
                    value2 = row[2]
                    value3 = row[23]
                    value4 = row[44]
                    value5 = row[45]
                    row_dict = {
                        "Band": value1,
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
                        print()
                        print("Band:", row["Band"])
                        print("Model name:", row["Model name"])
                        print("RAM:", row["RAM"])
                        print("Market region:", row["Market regions"])
                        print("Date of addition:", row["Date of addition"])
                        print("-----------------------------------------------------------------------------------------------------------------------------------")

                    if end_pos >= len(result_rows):
                        print("No more rows available.")
                        break

                    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()  # Convert input to lowercase
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



def get_ram_capacity_details(loaded_data):
    while True:
        try:
            result_rows = []
            ram_size = input("Enter the RAM size: ")  # Add error handling for non-integer input

            # Create a flag to check if the RAM size is found
            ram_size_found = False

            # Loop through each row in the CSV data
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
                        print()
                        print("OEM Id:", row["OEM Id"])
                        print("Release date:", row["Release date"])
                        print("Announcement date:", row["Announcement date"])
                        print("Dimensions:", row["Dimensions"])
                        print("Device category:", row["Device category"])
                        print("---------------------------------------------------------------------------------------------------------")

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
        except Exception as e:
            print(f"An error occurred: {e}")




def return_ordered_device_details(loaded_data):
    try:
        result_rows = []

        while True:
            # List of available brands
            brands = ["Samsung", "Xiaomi", "Sharp", "Sony", "Lenovo", "Asus", "BBK", "T-Mobile", "ZTE", "Nokia", "Microsoft", "LG", "Apple", "Motorola"]
            brand_string = ", ".join(brands)
            print(f"We have the following brand of phones:\n{brand_string}")

            brand_name = input("Enter the brand name (or 'quit' to exit): ").strip().lower()

            if brand_name == 'quit':
                break

            # List of available device types
            device_types = ["Tablet", "Smartwatch", "Smartphone"]

            print("We have the following device types:")
            for device_type in device_types:
                print(device_type)

            device_type = input("Enter the device type: ").strip().lower()

            # Input validation for price range
            while True:
                try:
                    min_price = float(input("Enter the minimum price for your phone: "))
                    max_price = float(input("Enter the maximum price for your phone: "))
                    break
                except ValueError:
                    print("Please enter valid numeric values for price.")

            # Function to manually parse the date
            def parse_date(date_string):
                day, month, year = map(int, date_string.split('-'))
                return (year, month, day)

            # Loop through your data to find matching devices
            for row in loaded_data:
                if row[1].strip().lower() == brand_name and row[9].strip().lower() == device_type:
                    price = float(row[15])
                    if min_price <= price <= max_price:
                        value1 = row[43]
                        value2 = row[24]
                        value3 = row[19]
                        value4 = row[29]
                        value5 = row[35]
                        value6 = parse_date(row[3])
                        value7 = row[15]
                        row_dict = {
                            "Battery Capacity": value1,
                            "Storage Space": value2,
                            "Additional Software Details": value3,
                            "Pixel Density": value4,
                            "Sim-Card-Type": value5,
                            "Released Date": value6,
                            "Price": value7
                        }
                        result_rows.append(row_dict)

            # Sort the result_rows by the 'Released Date'
            result_rows = sorted(result_rows, key=lambda x: x["Released Date"])

            # Check if any matching devices were found
            if not result_rows:
                print("No match for the given criteria.")
                try_another_option = input("Do you want to try another option? (yes/no): ").strip().lower()
                if try_another_option == 'no':
                    break
            else:
                num_rows = 20
                start_pos = 0

                while start_pos < len(result_rows):
                    end_pos = start_pos + num_rows
                    for i in range(start_pos, end_pos):
                        if i < len(result_rows):
                            row = result_rows[i]
                            print()
                            print("Released Date:", row["Released Date"])
                            print("Price:", row["Price"])
                            print("Battery Capacity: ", row["Battery Capacity"])
                            print("Storage Space: ", row["Storage Space"])
                            print("Additional Software Details: ", row["Additional Software Details"])
                            print("Pixel Density: ", row["Pixel Density"])
                            print("Sim-Card-Type: ", row["Sim-Card-Type"])
                            print("---------------------------------------------------------------------------------------------------------------------------")

                    if end_pos >= len(result_rows):
                        print("No more rows available.")
                        break

                    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").strip().lower()
                    if user_input == 'next':
                        start_pos += num_rows
                    elif user_input == 'quit':
                        print("The display of results is stopping...")
                        print("Stopped")
                        return 

    except Exception as e:
        print(f"An error occurred: {str(e)}")






