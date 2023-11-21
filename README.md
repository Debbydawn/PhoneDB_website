# PhoneDB - Mobile Device Data Analysis and Visualization

## Overview

In an era dominated by technological advancements, the intricacies of mobile devices play a pivotal role in shaping our digital landscape. The PhoneDB project is a comprehensive tool designed to retrieve, analyze, and visualize data on various mobile devices from a CSV file.

The project focuses on three main components:
1. **Data Retrieval:** Loading and retrieving specific details about devices based on various criteria.
2. **Data Analysis:** Utilizing pandas to analyze and derive meaningful insights from the dataset.
3. **Data Visualization:** Employing matplotlib to create visualizations that showcase trends and patterns in mobile device data.

## Project Structure

The project is organized into five modules:
1. **Loading_dataset.py:** Functions for loading the dataset in CSV format.
2. **Tui.py:** Text-based user interface and main menu.
3. **Data_retriever.py:** Functions for retrieving specific details from the dataset.
4. **Data_analysis.py:** Functions for analyzing the dataset using pandas.
5. **Data_visualization.py:** Functions for visualizing insights using matplotlib.

The main entry point is the `main.ipynb` Jupyter notebook, which orchestrates the execution of the PhoneDB program.

## How to Run

1. Ensure you have Python and Jupyter Notebook installed.
2. Clone the repository: `git clone https://github.com/your-username/PhoneDB.git`
3. Navigate to the project directory: `cd PhoneDB`
4. Open the `main.ipynb` notebook using Jupyter Notebook.

## Requirements

- COM728 environment
- Python
- Jupyter Notebook
- pandas
- matplotlib

Install the required dependencies using: `pip install -r requirements.txt`

## Functionality

### Data Retrieval
- `Get_oem_id_details(loaded_data)`: Retrieve details for a specified OEM ID.
- `Get_code_name_details(loaded_data)`: Retrieve details for devices associated with a specified code name.
- `Get_ram_capacity_details(loaded_data)`: Retrieve details based on a specified RAM capacity.
- `Return_ordered_device_details(loaded_data)`: Retrieve ordered device details based on brand, device type, and price range.

### Data Analysis
- `Get_brand_regions(loaded_data_pd)`: Identify top regions where a specific brand of devices was sold.
- `Calculate_average_price_for_brand(loaded_data_pd)`: Analyze the average price of devices within a specific brand.
- `Average_mass_brand(loaded_data_pd)`: Analyze the average mass for each manufacturer.
- `Get_cheapest_prices_and_calculate_ratio(loaded_data_pd)`: Identify top 5 cheapest prices for a specific brand and calculate price-performance ratio.

### Data Visualization
- `Ram_type_proportion(loaded_data_pd)`: Visualize the proportion of RAM types using a pie chart.
- `Usb_connector_comparison(loaded_data_pd)`: Visualize the counts of different USB connector types using a bar chart.
- `Subplot_GBP(loaded_data_pd)`: Visualize monthly average price trends for devices released from 2020 to 2023 using subplots.
- `Vis_brand(loaded_data_pd)`: Visualize brand-wise battery capacity and the relationship between display size and battery capacity.
- `Average_ppr(loaded_data_pd)`: Visualize the average price performance ratio by brand for all the available brands

### Project Execution
- Run the functions provided in the `main.ipynb` notebook to interact with the PhoneDB application.

## Contributors

- Deborah Adedigba (https://github.com/DeborahAdedigba)

## License

This project is licensed under the [MIT License](LICENSE).
