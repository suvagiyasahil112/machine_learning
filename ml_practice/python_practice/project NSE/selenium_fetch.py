from selenium import webdriver
import time
import os
import pandas as pd
from datetime import datetime, timedelta
# Function to download Bhavcopy CSV for a specific date
def download_bse_bhavcopy(bse_driver, bse_date_str, bse_download_dir):
    bse_csv_filename = f'BhavCopy_BSE_FO_0_0_0_{bse_date_str.replace("-", "")}_F_0000.CSV'
    bse_csv_filepath = os.path.join(bse_download_dir, bse_csv_filename)
    if os.path.exists(bse_csv_filepath):
        print(f"File already exists for {bse_date_str}")
        return bse_csv_filepath
    try:
        bse_url = f'https://www.bseindia.com/download/Bhavcopy/Derivative/BhavCopy_BSE_FO_0_0_0_{bse_date_str.replace("-", "")}_F_0000.CSV'
        bse_driver.get(bse_url)
        time.sleep(6)  # Adjust the sleep time as needed
        if os.path.exists(bse_csv_filepath):
            return bse_csv_filepath
    except Exception as bse_e:
        print(f"Error downloading Bhavcopy for {bse_date_str}: {bse_e}")
    return None
# Get the date range from the user
bse_start_date_input = input('Enter the start date (dd-mm-yyyy): ')
bse_end_date_input = input('Enter the end date (dd-mm-yyyy): ')
# Convert the input dates to datetime objects
bse_start_date = datetime.strptime(bse_start_date_input, '%d-%m-%Y')
bse_end_date = datetime.strptime(bse_end_date_input, '%d-%m-%Y')
bse_dfs = []
# Set up Chrome options to handle downloads
bse_download_dir = r'C:\Users\SMIT\Downloads\iRage Assignment\BSE Data'
bse_chrome_options = webdriver.ChromeOptions()
bse_prefs = {'download.default_directory': bse_download_dir}
bse_chrome_options.add_experimental_option('prefs', bse_prefs)
# Set up the Selenium WebDriver
bse_driver = webdriver.Chrome(options=bse_chrome_options)
# Loop over the date range and download files
bse_current_date = bse_start_date
while bse_current_date <= bse_end_date:
    bse_date_str = bse_current_date.strftime('%Y-%m-%d')
    bse_csv_filepath = download_bse_bhavcopy(bse_driver, bse_date_str, bse_download_dir)
    if bse_csv_filepath:
        bse_df = pd.read_csv(bse_csv_filepath)
        bse_dfs.append(bse_df)
    else:
        print(f"Skipping {bse_date_str} (file not found)")
    bse_current_date += timedelta(days=1)
bse_driver.quit()
# Concatenate all DataFrames into one
if bse_dfs:
    bse_compiled_df = pd.concat(bse_dfs, ignore_index=True)
    bse_compiled_csv_filepath = os.path.join(bse_download_dir, f'Compiled_BSE_BhavCopies.csv')
    bse_compiled_df.to_csv(bse_compiled_csv_filepath, index=False)
    print(f"All BSE Derivative Bhavcopy files compiled into: {bse_compiled_csv_filepath}")
else:
    print("No BSE Derivative Bhavcopy file was downloaded.")
