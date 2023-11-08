
def run_phoneDB_program():
    print("Welcome to PhoneDB Website")
    username = input("What is your name? ")
    username = username.upper()
    print(f"\nYes, {username}, let's get to work.")
    import Data_retriever
    import Data_analysis
    import Data_visualization
    


    while True:
        print("\nPlease select a section:")
        print("A. Work with a CSV file")
        print("B. Work with a Pandas file")
        print("C. Visualize using the pandas data")

        try:
            choice1 = input("Enter the section (A-C): ").upper()
            
            if choice1 == "A":
                print("\nPlease select an operation:")
                print("1. Load the data from a CSV file")
                print("2. Get some details on an individual device by oem_id")
                print("3. Get details of all devices for a specified code name")
                print("4. Get details of all devices for a specified RAM capacity")
                print("5. Get details of all devices for a specified brand, category and price range")
                choice_A = int(input("Enter your choice (1-5): "))

                if choice_A == 1:
                    # Perform option 1
                    print("Option 1 selected.")
                    loaded_data = load_csv_file()

                elif choice_A == 2:
                    # Perform option 2
                    print("Option 2 selected.")
                    from Data_retriever import get_oem_id_details
                    # host_details = get_host_details()
                    device_details = Data_retriever.get_oem_id_details(loaded_data)
                    print(device_details)

                elif choice_A == 3:
                    # Perform option 3
                    print("Option 3 selected.")
                    from Data_retriever import get_code_name_details
                    code_name = Data_retriever.get_code_name_details(loaded_data)
                    print(code_name)

                elif choice_A == 4:
                    # Perform option 4
                    print("Option 4 selected.")
                    from Data_retriever import get_ram_capacity_details
                    ram = Data_retriever.get_ram_capacity_details(loaded_data)
                    print(ram)
                elif choice_A == 5:
                    # Perform option 5
                    print("Option 5 selected.")
                    from Data_retriever import return_ordered_device_details
                    ordered_detiails = Data_retriever.return_ordered_device_details(loaded_data)
                    print(ordered_detiails)

                else:
                    print("Invalid choice. Please enter a valid option.")

            elif choice1 == "B":
                print("\nPlease select an operation:")
                print("5. Load your data from a CSV file into a pandas DataFrame")
                print("6. Get the top 5 regions a brand is sold")
                print("7. Get the average price of devices for a brand in a particular or all currencies")
                print("8. Get the average mass of device for each manufacturer")
                print("9. Get the recommendation from the top 5 cheap device with a price performance ratio")
                choice_B = int(input("Enter your choice (5-9): "))

                if choice_B == 5:
                    # Perform option 5
                    print("Option 5 selected.")
                    loaded_data_pd = load_pd_file()

                elif choice_B == 6:
                    # Perform option 6
                    print("Option 6 selected.")
                    from Data_analysis import get_brand_regions
                    brand_region = Data_analysis.get_brand_regions(loaded_data_pd)
                    print(brand_region)

                elif choice_B == 7:
                    # Perform option 7
                    print("Option 7 selected.")
                    from Data_analysis import calculate_average_price_for_brand
                    average_price = Data_analysis.calculate_average_price_for_brand(loaded_data_pd)
                    print(average_price)

                elif choice_B == 8:
                    # Perform option 8
                    print("Option 8 selected.")
                    from Data_analysis import average_mass_brand
                    average_mass = Data_analysis.average_mass_brand(loaded_data_pd)
                    print(average_mass)
                    
                elif choice_B == 9:
                    # Perform option 9
                    print("Option 9 selected.")
                    from Data_analysis import get_cheapest_prices_and_calculate_ratio
                    ratio = Data_analysis.get_cheapest_prices_and_calculate_ratio(loaded_data_pd)
                    print(ratio)

                else:
                    print("Invalid choice. Please enter a valid option.")

            elif choice1 == "C":
                print("\nPlease select an operation:")
                print("9. Get the proportion of the RAM types for devices in the current market using a pie chart")
                print("10. Get the number of number of devices for each USB connector type using a bar chart")
                print("11. Get the monthly average price trends (in GBP) for devices released in each year from 2020 to 2023.")
                print("12. Get bar chart for the average battery capacity and relationship between display size and battery capacity with a scatter plot")
                choice_C = int(input("Enter your choice (9-12): "))

                if choice_C == 9:
                    # Perform option 9
                    print("Option 9 selected.")
                    from Data_visualization import ram_type_proportion
                    pie_chart = Data_visualization.ram_type_proportion(loaded_data_pd)

                elif choice_C == 10:
                    # Perform option 10
                    print("Option 10 selected.")
                    from Data_visualization import usb_connector_comparison
                    bar_chart = Data_visualization.usb_connector_comparison(loaded_data_pd)

                elif choice_C == 11:
                    # Perform option 11
                    print("Option 11 selected.")
                    from Data_visualization import subplot_GBP
                    plot_subplot = Data_visualization.subplot_GBP(loaded_data_pd)

                elif choice_C == 12:
                    # Perform option 12
                    print("Option 12 selected.")
                    from Data_visualization import vis_brand
                    plot_vis = Data_visualization.vis_brand(loaded_data_pd)

                else:
                    print("Invalid choice. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        # Ask the user if they want to continue or exit
        continue_choice = input("Do you want to perform another operation? (yes/no): ")
        
        if continue_choice.lower() != 'yes':
            print("Exiting...\nExited")
            break


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







