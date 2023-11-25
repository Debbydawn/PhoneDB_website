# reading in the csv data from csv file using csv module
import csv
file_location = None  # Initialize the location variable

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
            print("\n\033[1mFetching data...\033[0m")
            print(f"Successfully loaded the \033[1m{file_location}\033[0m dataset.")
            return phone_data

        except csv.Error:
            print(f"\033[1m\033[31mInvalid CSV file:\033[0m {file_location}")
        except FileNotFoundError:
            print(f"\033[1m\033[31mFile not found:\033[0m {file_location}")
        except IOError:
            print(f"\033[1m\033[31mCouldn't read\033[0m {file_location}.")

        retry = input("Do you want to enter a new file location? (yes/no): ")
        if retry.lower() != 'yes':
            print("\033[1mExiting file loading...\033[0m\n")
            return None  # Returning None to indicate an unsuccessful attempt

        
        
import pandas as pd        
# Reading in the csv data as a pandas file using pandas
def load_pd_file():
    global file_location  # Use the global variable
    if file_location is not None:
        try:
            phone_data = pd.read_csv(file_location, encoding='utf-8')
            print("\n\033[1mFetching data...\033[0m")
            print(f"Successfully loaded the \033[1m{file_location}\033[0m pandas dataset.")
            return phone_data
        except pd.errors.EmptyDataError:
            print(f"\033[1m\033[31mEmpty CSV file:\033[0m {file_location}")
        except FileNotFoundError:
            print(f"\033[1m\033[31mFile not found:\033[0m {file_location}")
        except pd.errors.ParserError:
            print(f"\033[1m\033[31mCouldn't read\033[0m {file_location}. It may not be a valid CSV file.")
        except Exception as e:
            print(f"\033[1m\033[31mAn error occurred while loading the file:\033[0m {str(e)}")
