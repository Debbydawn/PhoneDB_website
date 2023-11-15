def run_phoneDB_program():
    print("\033[1m\033[34mWelcome to PhoneDB!\033[0m")
    print("\033[1m\033[4mBrief Background\033[0m")
    print("\033[32mPhoneDB website is your go-to information hub for smartphones, tablets, PDAs, and mobile devices.\033[0m")
    print("\033[32mOur platform offers a comprehensive collection of data and various services to help you find the most suitable mobile device.\033[0m")
    print()
    print("\033[1m\033[31mThank you for choosing PhoneDB! Let's explore the world of mobile devices together.\033[0m")

   

    username = input("What is your name? ")
    username = username.upper()
    print(f"\nYes, {username}, let's get to work.")
    import Loading_dataset  # Assuming the Loading_dataset module contains the load_csv_file and load_pd_file functions
    import Data_retriever
    import Data_analysis
    import Data_visualization

    loaded_data = None
    loaded_data_pd = None

    while True:
        try:
            print("\nPlease select a section:")
            print("A. Work with a CSV file")
            print("B. Work with a Pandas file")
            print("C. Visualize using the pandas data")

            choice1 = input("Enter the section (A-C): ").upper()

            while choice1 not in ['A', 'B', 'C']:
                print("Invalid choice. Please enter a valid option (A-C).")
                choice1 = input("Enter the section (A-C): ").upper()

            if choice1 == "A":
                while True:
                    print("\nPlease select an operation:")
                    print("1. Load the data from a CSV file")
                    print("2. Get some details on an individual device by oem_id")
                    print("3. Get details of all devices for a specified code name")
                    print("4. Get details of all devices for a specified RAM capacity")
                    print("5. Get details of all devices for a specified brand, category, and price range")
                    choice_A = int(input("Enter your choice (1-5): "))

                    if choice_A == 1:
                        # Perform option 1
                        print("Option 1 selected.")
                        loaded_data = Loading_dataset.load_csv_file()

                    elif choice_A == 2:
                        # Perform option 2
                        print("Option 2 selected.")
                        from Data_retriever import get_oem_id_details
                        device_details = Data_retriever.get_oem_id_details(loaded_data)

                    elif choice_A == 3:
                        # Perform option 3
                        print("Option 3 selected.")
                        from Data_retriever import get_code_name_details
                        code_name = Data_retriever.get_code_name_details(loaded_data)

                    elif choice_A == 4:
                        # Perform option 4
                        print("Option 4 selected.")
                        from Data_retriever import get_ram_capacity_details
                        ram = Data_retriever.get_ram_capacity_details(loaded_data)
                        
                    elif choice_A == 5:
                        # Perform option 5
                        print("Option 5 selected.")
                        from Data_retriever import return_ordered_device_details
                        ordered_details = Data_retriever.return_ordered_device_details(loaded_data)
                        

                    else:
                        print("Invalid choice. Please enter a valid option.")

                    # Ask the user if they want to continue in section A
                    continue_choice_A = input("Do you want to perform another operation in section A? (yes/no): ").lower()
                    while continue_choice_A not in ['yes', 'no']:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
                        continue_choice_A = input("Do you want to perform another operation in section A? (yes/no): ").lower()

                    if continue_choice_A == 'no':
                        print("Returning to the main menu...")
                        break


            elif choice1 == "B":
                if loaded_data is None:
                    print("Please load the dataset first in Section A.")
                else:
                    while True:
                        print("\nPlease select an operation:")
                        print("5. Load your data from a CSV file into a pandas DataFrame")
                        print("6. Get the top 5 regions a brand is sold")
                        print("7. Get the average price of devices for a brand in a particular or all currencies")
                        print("8. Get the average mass of the device for each manufacturer")
                        print("9. Get the recommendation from the top 5 cheap devices with a price performance ratio")
                        choice_B = int(input("Enter your choice (5-9): "))

                        if choice_B == 5:
                            # Perform option 5
                            print("Option 5 selected.")
                            # file_location = input("Enter the file location: ")
                            loaded_data_pd = Loading_dataset.load_pd_file()

                        elif choice_B == 6:
                            # Perform option 6
                            print("Option 6 selected.")
                            from Data_analysis import get_brand_regions
                            brand_region = Data_analysis.get_brand_regions(loaded_data_pd)
                            

                        elif choice_B == 7:
                            # Perform option 7
                            print("Option 7 selected.")
                            from Data_analysis import calculate_average_price_for_brand
                            average_price = Data_analysis.calculate_average_price_for_brand(loaded_data_pd)
                            

                        elif choice_B == 8:
                            # Perform option 8
                            print("Option 8 selected.")
                            from Data_analysis import average_mass_brand
                            average_mass = Data_analysis.average_mass_brand(loaded_data_pd)
                            

                        elif choice_B == 9:
                            # Perform option 9
                            print("Option 9 selected.")
                            from Data_analysis import get_cheapest_prices_and_calculate_ratio
                            ratio = Data_analysis.get_cheapest_prices_and_calculate_ratio(loaded_data_pd)
                            

                        else:
                            print("Invalid choice. Please enter a valid option.")

                        # Ask the user if they want to continue in section B
                        continue_choice_B = input("Do you want to perform another operation in section B? (yes/no): ").lower()
                        while continue_choice_B not in ['yes', 'no']:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
                            continue_choice_B = input("Do you want to perform another operation in section B? (yes/no): ").lower()

                        if continue_choice_B == 'no':
                            print("Returning to the main menu...")
                            break

            elif choice1 == "C":
                while True:
                    try:
                        if loaded_data_pd is None:
                            print("Please load the dataset first in Section B.")
                            break

                        print("\nPlease select an operation:")
                        print("9. Get the proportion of the RAM types for devices in the current market using a pie chart")
                        print("10. Get the number of devices for each USB connector type using a bar chart")
                        print("11. Get the monthly average price trends (in GBP) for devices released in each year from 2020 to 2023.")
                        print("12. Get a bar chart for the average battery capacity and the relationship between display size and battery capacity with a scatter plot")

                        choice_C = int(input("Enter your choice (9-12): "))

                        while choice_C not in [9, 10, 11, 12]:
                            print("Invalid choice. Please enter a valid option (9-12).")
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

                        # Ask the user if they want to continue in section C
                        continue_choice_C = input("Do you want to perform another operation in section C? (yes/no): ").lower()
                        while continue_choice_C not in ['yes', 'no']:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
                            continue_choice_C = input("Do you want to perform another operation in section C? (yes/no): ").lower()

                        if continue_choice_C == 'no':
                            print("Returning to the main menu...")
                            break

                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        # Ask the user if they want to return to the main menu or exit
        return_choice = input("Do you want to return to the main menu or exit the program? (menu/exit): ")
        if return_choice.lower() == 'exit':
            print("Exiting...\nExited")
            break
        elif return_choice.lower() != 'menu':
            print("Invalid choice. Returning to the main menu...")