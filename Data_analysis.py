# loading dataset
from Loading_dataset import load_pd_file

#B1

def get_brand_regions(loaded_data_pd):
    while True:
        try:
            brand_names = ", ".join(loaded_data_pd['brand'].unique())
            print(f"Available device brand names in this dataset:\n{brand_names}")

            user_brand = input("Enter the brand you want to see (or 'quit' to exit): ").strip().lower()

            if user_brand == 'quit':
                break  # Exit the loop if the user wants to quit

            # Validate user input against available brand names
            if user_brand not in loaded_data_pd['brand'].str.lower().unique():
                raise ValueError("Invalid brand name. Please enter a valid brand name.")

            # Group data to find the top regions for each brand
            brand_counts = loaded_data_pd.groupby(['market_regions', 'brand']).size().reset_index(name='counts')
            top_regions_by_brand = brand_counts.groupby('brand').apply(lambda x: x.nlargest(5, 'counts'))
            top_regions_by_brand = top_regions_by_brand.drop(columns='brand').reset_index()

            user_brand_data = top_regions_by_brand[top_regions_by_brand['brand'].str.lower() == user_brand]

            if not user_brand_data.empty:
                print(f"Top regions for brand: {user_brand}")
                for _, row in user_brand_data.iterrows():
                    print(f"Region: {row['market_regions']} - Count: {row['counts']}")
            else:
                print(f"No data available for brand: {user_brand}")

        except ValueError as ve:
            print(f"\033[31mValueError: {ve}. Please try again.\033[0m")
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}. Please try again.\033[0m")




# B2

def calculate_average_price_for_brand(loaded_data_pd):
    while True:
        try:
            # Get user input for the brand
            brand_name = ", ".join(loaded_data_pd['brand'].unique())
            print(f"The device brand names in this dataset are:\n {brand_name}")

            brand_input = input("Enter the brand (or 'all' for all brands): ").strip().lower()
            valid_brand_options = loaded_data_pd['brand'].str.lower().unique()

            while brand_input not in valid_brand_options:
                print(f"Invalid input. Please choose from the following options: {', '.join(valid_brand_options)}")
                brand_input = input("Enter the brand (or 'all' for all brands): ").strip().lower()

            # Get user input for the currency
            currency = ", ".join(loaded_data_pd['price_currency'].unique())
            print(f"These are the currencies you can choose from: \n {currency}")

            currency_input = input("Enter the currency (or 'all' for all currencies): ").strip().lower()
            valid_currency_options = loaded_data_pd['price_currency'].str.lower().unique()

            while currency_input not in valid_currency_options:
                print(f"Invalid input. Please choose from the following options: {', '.join(valid_currency_options)}")
                currency_input = input("Enter the currency (or 'all' for all currencies): ").strip().lower()

            # Filter the data based on user input
            filtered_data = loaded_data_pd.copy()  # Create a copy of the original data to avoid modifying it

            if brand_input != 'all':
                filtered_data = filtered_data[filtered_data['brand'].str.lower() == brand_input]

            if currency_input != 'all':
                filtered_data = filtered_data[filtered_data['price_currency'].str.lower() == currency_input]

            if filtered_data.empty:
                print(f"No data found for brand: '{brand_input}' and currency: '{currency_input}'")
            else:
                # Group the filtered data by 'brand' and 'price_currency' and calculate the average price for each combination
                brand_avg_prices = filtered_data.groupby(['brand', 'price_currency'])['price'].mean().round(2).reset_index()

                if not brand_avg_prices.empty:
                    num_rows = 20
                    start_pos = 0
                    end_pos = min(start_pos + num_rows, len(brand_avg_prices))

                    while True:
                        # Display the current set of rows
                        print(brand_avg_prices.iloc[start_pos:end_pos])

                        if end_pos >= len(brand_avg_prices):
                            print("\033[1mNo more rows available.\033[0m")
                            break

                        user_input = input("Enter 'next' to retrieve the next 20 rows, or 'quit' to exit: ").strip().lower()
                        if user_input == 'next':
                            start_pos += num_rows
                            end_pos = min(start_pos + num_rows, len(brand_avg_prices))
                        elif user_input == 'quit':
                            break

                    retry = input("Would you like to calculate for another brand/currency (yes/no)? ").strip().lower()
                    if retry != 'yes':
                        break
                else:
                    print("\nNo data available for average price by brand and currency.")

        except Exception as e:
            print(f"\033[31mAn error occurred: {e}. Please try again.\033[0m")
            return None


# B3

def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from the following options: {', '.join(valid_options)}")

def average_mass_brand(loaded_data_pd):
    try:
        # Group the data by 'manufacturer' and calculate the average 'weight_gram'
        manufact_avg_mass = loaded_data_pd.groupby('manufacturer')['weight_gram'].mean().round(2).reset_index()

        if not manufact_avg_mass.empty:
            num_rows = 20
            start_pos = 0
            end_pos = min(start_pos + num_rows, len(manufact_avg_mass))

            while True:
                # Display the current set of rows without external modules
                print("\033[1mAverage Mass by Brand\033[0m")
                print(f"\033[4m\033[1m{'Manufacturer':<30}{'Average Weight (grams)':<20}\033[0m")

                for _, row in manufact_avg_mass.iloc[start_pos:end_pos].iterrows():
                    print(f"{row['manufacturer']:<40}{row['weight_gram']:<25}")

                if end_pos >= len(manufact_avg_mass):
                    print("\033[1mNo more rows available.\033[0m")
                    break

                user_input = get_user_input("\nEnter 'next' to view the next 20 rows or 'quit' to exit: ", ['next', 'quit'])

                if user_input == 'next':
                    start_pos += num_rows
                    end_pos = min(start_pos + num_rows, len(manufact_avg_mass))
                elif user_input == 'quit':
                    break
        else:
            print("\nNo data available for average mass by brand.")
    
    except Exception as e:
        print(f"\n\033[31mAn error occurred: {e}. Please try again.\033[0m")
        # Return None in case of an error
        return None

#B4

"""  Display the top 5 cheapest prices for a specified brand and calculate the price-performance ratio for a selected device.

    Parameters:
    - loaded_data_pd (pd.DataFrame): The loaded dataset in a Pandas DataFrame.

    """
def get_cheapest_prices_and_calculate_ratio(loaded_data_pd):
    while True:
        try:
            brand_names = ", ".join(loaded_data_pd['brand'].unique())
            print(f"Available device brand names in this dataset:\n{brand_names}")

            user_brand = input("Enter the brand to find the top 5 cheapest prices (or 'quit' to exit): ").strip().lower()

            if user_brand == 'quit':
                return  # Exit the function if the user wants to quit

            filtered_data = loaded_data_pd[loaded_data_pd['brand'].str.lower() == user_brand]

            if not filtered_data.empty:
                top_5_cheapest = filtered_data.nsmallest(5, 'price')[['oem_id', 'price']]
                print(f"Top 5 cheapest prices for brand: {user_brand}")
                for _, row in top_5_cheapest.iterrows():
                    print(f"OEM ID: {row['oem_id']} - Price: {row['price']}")

                user_id_input = input("Enter the OEM ID of the device to calculate the price-performance ratio (or 'quit' to return to brand selection): ").strip()

                if user_id_input == 'quit':
                    return  # Return to brand selection

                # Validate the entered OEM ID
                if user_id_input not in loaded_data_pd['oem_id'].values:
                    print(f"Invalid OEM ID: {user_id_input}. Please enter a valid OEM ID.")
                else:
                    calculate_price_performance_ratio(loaded_data_pd, user_id_input)
                    break  # Exit the loop after a successful calculation
            else:
                print(f"No data available for brand: {user_brand}")
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}. Please try again.\033[0m")

        
        
"""
    Calculate and display the price-performance ratio for a selected device.

    Parameters:
    - loaded_data_pd (pd.DataFrame): The loaded dataset in a Pandas DataFrame.
    - user_id_input (str): The user-entered OEM ID of the device.
    """

def calculate_price_performance_ratio(loaded_data_pd, user_id_input):
    df = loaded_data_pd

    # Define weightage factors
    weight_cpu = 0.4
    weight_ram = 0.3
    weight_storage = 0.2
    weight_price = 0.1

    # Calculate a performance score based on specifications
    df['Performance_Score'] = (weight_cpu * df['cpu_clock']) + \
                               (weight_ram * df['ram_capacity']) + \
                               (weight_storage * df['non_volatile_memory_capacity'])

    # Calculate price-performance ratio
    df['Price_Performance_Ratio'] = df['Performance_Score'] / df['price']

    # Normalize the price-performance ratios
    df['Normalized_Price_Performance'] = (df['Price_Performance_Ratio'] - df['Price_Performance_Ratio'].min()) / \
                                        (df['Price_Performance_Ratio'].max() - df['Price_Performance_Ratio'].min())

    # Sort the devices by their normalized price-performance ratios
    df = df.sort_values(by='Normalized_Price_Performance', ascending=False)

    # Find and display information about the specified device
    selected_device = df[df['oem_id'] == user_id_input]
    if not selected_device.empty:
        brand = selected_device['brand'].values[0]
        price = selected_device['price'].values[0]
        performance_score = selected_device['Performance_Score'].values[0]
        price_performance_ratio = selected_device['Price_Performance_Ratio'].values[0]

        print()
        print(f"For this {brand} brand and OEM ID of {user_id_input} with a price of {price}:")
        print(f"The Performance score of the device is {performance_score:.2f}")
        print(f"The higher the number (up to {df['Performance_Score'].max():.2f}) the better the performance of the device.")
        print(f"The lower the number (down to {df['Performance_Score'].min():.2f}) the less the performance of the device.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print(f"The Price Performance Ratio for the device is {price_performance_ratio:.2f}")
        print(f"The higher the number (up to {df['Price_Performance_Ratio'].max():.2f}) the better the performance relative to the price.")
        print(f"The closer it is to (down to {df['Price_Performance_Ratio'].min():.2f}), the less the performance of the device for its price.")

        # Add recommendations based on the price-performance ratio
        if price_performance_ratio >= 5:  # Good buy threshold is 5.0
            print("This is a good buy! It offers great performance for its price.")
        else:
            print("Based on the price performance ratio. \nPlease consider other options. It may not provide the best value for your money.")
            print()
    else:
        print(f"No device with OEM ID {user_id_input} found in the dataset.")
   