# loading dataset
from Loading_dataset import load_csv_file

# A1
# function to return the specific details based on OEM_id of a device
def get_oem_id_details(loaded_data):
    while True:
        try:
            oem_id = input("Enter the OEM ID: ").lower()  # Convert input to lowercase

            # creating a dictionary to store the details
            oem_details = {}

            # Loop through each row in the CSV file
            for row in loaded_data:
                # Check if the row has enough elements and compare in lowercase
                if row and len(row) > 0 and row[0].lower() == oem_id:
                    # If the OEM ID is found, store the details in the dictionary
                    oem_details["OEM ID"] = oem_id
                    oem_details["Model"] = row[2] if len(row) > 2 else ""
                    oem_details["Manufacturer"] = row[6] if len(row) > 6 else ""
                    oem_details["Weight"] = row[14] if len(row) > 14 else ""
                    oem_details["Price"] = row[15] if len(row) > 15 else ""
                    oem_details["Price Unit"] = row[16] if len(row) > 16 else ""

                    # Print the OEM ID before "OEM ID Details"
                    print("\033[44m\033[1m" + f"{oem_id} OEM ID Details:" + "\033[0m")
                    print("\033[1m" + "-" * 60 + "\033[0m")
                    print("\033[1mModel:\033[0m", oem_details["Model"])
                    print("\033[1mManufacturer:\033[0m", oem_details["Manufacturer"])
                    print("\033[1mWeight:\033[0m", oem_details["Weight"])
                    print("\033[1mPrice:\033[0m", oem_details["Price"], oem_details["Price Unit"])
                    print("\033[1m" + "-" * 60 + "\033[0m")

                    return  # Exit the function

            # If the loop completes without finding a match
            print("\033[1m" + "No match for the OEM ID details found." + "\033[0m")
            retry = input("Do you want to enter a new OEM ID? (yes/no): ")
            if retry.lower() != 'yes':
                print("\033[1m" + "Exiting OEM ID details retrieval..." + "\033[0m\n")
                break  # Exit the loop to stop asking for a new OEM ID

        except ValueError:
            print("\033[41m\033[1m" + "Invalid input. Please enter a valid OEM ID." + "\033[0m")
        except IndexError:
            print("\033[41m\033[1m" + "Index error. Make sure your data has enough columns." + "\033[0m")
        except Exception as e:
            print("\033[41m\033[1m" + f"An error occurred: {e}" + "\033[0m")




# A2     
# function to get code_name from user and return specific details about the code names 
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
                print("\033[1mNo match for the code name details found.\033[0m")
            else:
                num_rows = 20
                start_pos = 0
                end_pos = min(start_pos + num_rows, len(result_rows))

                while True:
                    for i in range(start_pos, end_pos):
                        row = result_rows[i]
                        print()
                        print("\033[1m" + "-" * 100 + "\033[0m")
                        print("\033[1mBand:\033[0m", row["Band"])
                        print("\033[1mModel name:\033[0m", row["Model name"])
                        print("\033[1mRAM:\033[0m", row["RAM"])
                        print("\033[1mMarket region:\033[0m", row["Market regions"])
                        print("\033[1mDate of addition:\033[0m", row["Date of addition"])

                    if end_pos >= len(result_rows):
                        print("\033[1m" + "-" * 100 + "\033[0m")
                        print("\033[1mNo more rows available.\033[0m")
                        break

                    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()

                    while user_input not in ['next', 'quit']:
                        print("\033[1mInvalid input.\033[0m Please enter 'next' to retrieve more rows or 'quit' to exit.")
                        user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ")

                    if user_input == 'next':
                        start_pos += num_rows
                        end_pos = min(start_pos + num_rows, len(result_rows))
                    elif user_input == 'quit':
                        print("\033[1mThe display of results is stopping...\033[0m")
                        print("\033[1mStopped\033[0m")
                        break
                # Break out of the while loop after displaying the results
                break
        except ValueError:
            print("\033[41m\033[1mInvalid input.\033[0m Please enter a valid code name (string).")



# A3

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
                print("\033[1mNo match for the RAM size details found.\033[0m")
            else:
                # displaying 20 rows at time if available 
                num_rows = 20
                start_pos = 0
                end_pos = min(start_pos + num_rows, len(result_rows))

                while True:
                    for i in range(start_pos, end_pos):
                        row = result_rows[i]
                        print()
                        print("\033[1m" + "-" * 100 + "\033[0m")
                        print("\033[1mOEM Id:\033[0m", row["OEM Id"])
                        print("\033[1mRelease date:\033[0m", row["Release date"])
                        print("\033[1mAnnouncement date:\033[0m", row["Announcement date"])
                        print("\033[1mDimensions:\033[0m", row["Dimensions"])
                        print("\033[1mDevice category:\033[0m", row["Device category"])

                    if end_pos >= len(result_rows):
                        print("\033[1m" + "-" * 100 + "\033[0m")
                        print("\033[1mNo more rows available.\033[0m")
                        break

                    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()

                    while user_input not in ['next', 'quit']:
                        print("\033[1mInvalid input.\033[0m Please enter 'next' to retrieve more rows or 'quit' to exit.")
                        user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()

                    if user_input == 'next':
                        start_pos += num_rows
                        end_pos = min(start_pos + num_rows, len(result_rows))
                    elif user_input == 'quit':
                        print("\033[1mThe display of results is stopping...\033[0m")
                        print("\033[1mStopped\033[0m")
                        break
                # Break out of the while loop after displaying the results
                break
        except Exception as e:
            print(f"An error occurred: {e}")





# A4
# extracts specific device details, and sorts the results by release date
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
                if len(row) > 43 and row[1].strip().lower() == brand_name and row[9].strip().lower() == device_type:
                    price = float(row[15]) if row[15] else 0.0
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
                print("\033[1mNo match for the given criteria.\033[0m")
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
                            print("\033[1mReleased Date:\033[0m", row["Released Date"])
                            print("\033[1mPrice:\033[0m", row["Price"])
                            print("\033[1mBattery Capacity:\033[0m", row["Battery Capacity"])
                            print("\033[1mStorage Space:\033[0m", row["Storage Space"])
                            print("\033[1mAdditional Software Details:\033[0m", row["Additional Software Details"])
                            print("\033[1mPixel Density:\033[0m", row["Pixel Density"])
                            print("\033[1mSim-Card-Type:\033[0m", row["Sim-Card-Type"])
                            print("\033[1m" + "-" * 135 + "\033[0m")

                    if end_pos >= len(result_rows):
                        print("\033[1m" + "-" * 100 + "\033[0m")
                        print("\033[1mNo more rows available.\033[0m")
                        break

                    user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()

                    while user_input not in ['next', 'quit']:
                        print("\033[1mInvalid input.\033[0m Please enter 'next' to retrieve more rows or 'quit' to exit.")
                        user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").lower()

                    if user_input == 'next':
                        start_pos += num_rows
                        end_pos = min(start_pos + num_rows, len(result_rows))
                    elif user_input == 'quit':
                        print("\033[1mThe display of results is stopping...\033[0m")
                        print("\033[1mStopped\033[0m")
                        break

    except Exception as e:
        print("\033[41m\033[1mAn error occurred:\033[0m", str(e))






