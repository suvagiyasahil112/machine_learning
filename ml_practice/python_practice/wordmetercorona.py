from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time
# Set up Chrome options
chrome_options = Options()

chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)


# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL for COVID-19 Worldometer page
url = "https://www.worldometers.info/coronavirus/"

# Open the page
driver.get(url)
# Wait for the table to load (top 10 countries table)
time.sleep(3)
# Locate the table containing the data
table = driver.find_element(By.XPATH, '//*[@id="main_table_countries_today"]/tbody[1]')
# Get the rows of the table (top 10 affected countries)
rows = table.find_elements(By.TAG_NAME, "tr")
# List to store the extracted data
data = []
# Loop through each row (top 10 countries)
for row in rows[1:11]:  # Skipping the first header row
    columns = row.find_elements(By.TAG_NAME, "td")
    country = columns[1].text
    total_cases = columns[2].text
    total_deaths = columns[4].text
    total_recoveries = columns[6].text
    active_cases = columns[8].text
    # Append data to the list
    data.append({
        "Country": country,
        "Total Cases": total_cases,
        "Total Deaths": total_deaths,
        "Total Recoveries": total_recoveries,
        "Active Cases": active_cases
    })
# Create a DataFrame from the extracted data
df = pd.DataFrame(data)
# Clean the DataFrame (convert to numeric values, remove commas, handle missing data)
def clean_and_convert_column(column):
    # Replace empty strings, "N/A", and commas with NaN
    column = column.replace({"": None, "N/A": None, ',': ''}, regex=True)
    # Convert the column to numeric values (invalid values will be converted to NaN)
    column = pd.to_numeric(column, errors='coerce')
    # Fill NaN values with 0
    return column.fillna(0).astype(int)
# Apply cleaning and conversion for each column
df['Total Cases'] = clean_and_convert_column(df['Total Cases'])
df['Total Deaths'] = clean_and_convert_column(df['Total Deaths'])
df['Total Recoveries'] = clean_and_convert_column(df['Total Recoveries'])
df['Active Cases'] = clean_and_convert_column(df['Active Cases'])
# Close the browser
driver.quit()
# Print cleaned data
print(df)