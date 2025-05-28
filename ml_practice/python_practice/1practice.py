import numpy  as np
import pandas as pd  
import matplotlib.pyplot as plt
import selenium
import seaborn as sns
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# *
# **
# ***
# ****
# *****


# for i in range (6):
#     print(i * "*")
    






# *****
# ****
# ***
# **
# *    
# for i in range (5,0,-1):
#     print(i * "*")






#     *    
#    ***   
#   *****  
#  ******* 
# *********

# for j in range (4,0,-1):
#     # print(" ")
#     for i in range (1,10,2):
#         # for j in range (4,0,-1):
#             print(i*"*")
#             break

# rows=5
# for i  in range(1,rows+1):
#     print(" "*(rows-i) , "*" * (2*i-1))

# rows=5
# for i in range (rows-1,0,-1):
#     print(" "*(rows-i),"*" * (2*i-1))


#     *
#    **
#   ***
#  ****
# *****

# rows = 5
# for i in range(1,rows+1):
#     print(" "*(rows-i) + "*"*i)


#------------------------ pandas-------------------------  



import random
import pandas as pd
import numpy as np
data = {
    'Company': ['Maruti Suzuki', 'Maruti Suzuki', 'Maruti Suzuki',
               'Hyundai', 'Hyundai', 'Hyundai',
               'Tata Motors', 'Tata Motors', 'Tata Motors',
               'Toyota', 'Toyota',
               'Honda', 'Honda'],
    'Name': ['Swift', 'Baleno', 'Dzire',
             'Creta', 'Venue', 'Verna',
             'Nexon', '3', 'Altroz',
             'Fortuner', 'Innova Crysta',
             'Amaze', 'City'],
    'Engine_CC': [1197, 1197, 1197,
                  1497, 1197, 1497,
                  1199, 1956, 1199,
                  2755, 2393,
                  1199, 1498],
    'Price': [750000, 650000, 850000,
              1350000, 800000, 1200000,
              950000, 1500000, 630000,
              4000000, 2000000,
              800000, 1300000],
    'Fuel_Type': ['Petrol/Diesel', 'Petrol', 'Petrol',
                  'Petrol/Diesel', 'Petrol/Diesel', 'Petrol/Diesel',
                  'Petrol/Diesel', 'Diesel', 'Petrol/Diesel',
                  'Diesel', 'Diesel',
                  'Petrol', 'Petrol/Diesel'],
    'Transmission': ['Manual/Automatic', 'Manual/Automatic', 'Manual/Automatic',
                     'Manual/Automatic', 'Manual/Automatic', 'Manual/Automatic',
                     'Manual/Automatic', 'Manual/Automatic', 'Manual',
                     'Automatic', 'Manual/Automatic',
                     'Manual/Automatic', 'Manual/Automatic'],
    'Quantity': [0, 1, 3, 4, 6, 2, 0, 2, 2, 3, 5, 2, 3],
    # 'Sr_number': [1,2,3,4,5,6,7,8,9,10,11,12,13]


}
additional_data = {
    'Company': [
        # Kia
        'Kia', 'Kia', 'Kia',
        # Mahindra
        'Mahindra', 'Mahindra', 'Mahindra',
        # Volkswagen
        'Volkswagen', 'Volkswagen', 'Volkswagen',
        # Ford
        'Ford', 'Ford', 'Ford',
        # Nissan
        'Nissan', 'Nissan',
        # MG
        'MG', 'MG', 'MG',
        # Renault
        'Renault', 'Renault', 'Renault',
        # Skoda
        'Skoda', 'Skoda', 'Skoda',
        # Jeep
        'Jeep', 'Jeep', 'Jeep',
        # Isuzu
        'Isuzu', 'Isuzu',
        # Tesla
        'Tesla', 'Tesla', 'Tesla',
        # BMW
        'BMW', 'BMW', 'BMW',
        # Audi
        'Audi', 'Audi', 'Audi',
        # Mercedes
        'Mercedes', 'Mercedes', 'Mercedes',
        # Volvo
        'Volvo', 'Volvo', 'Volvo',
        # Porsche
        'Porsche', 'Porsche', 'Porsche'
    ],
    'Name': [
        # Kia
        'Seltos', 'Sonet', 'Carnival',
        # Mahindra
        'XUV700', 'Thar', 'Scorpio N',
        # Volkswagen
        'Polo', 'Virtus', 'Taigun',
        # Ford
        'Ecosport', 'Endeavour', 'Figo',
        # Nissan
        'Magnite', 'Kicks',
        # MG
        'Hector', 'Astor', 'Gloster',
        # Renault
        'Kwid', 'Triber', 'Duster',
        # Skoda
        'Octavia', 'Superb', 'Kushaq',
        # Jeep
        'Compass', 'Meridian', 'Wrangler',
        # Isuzu
        'D-Max', 'MU-X',
        # Tesla
        'Model 3', 'Model Y', 'Model S',
        # BMW
        'X1', 'X5', '3 Series',
        # Audi
        'A3', 'Q5', 'Q7',
        # Mercedes
        'A-Class', 'E-Class', 'S-Class',
        # Volvo
        'XC40', 'XC60', 'XC90',
        # Porsche
        'Macan', 'Cayenne', '911 Carrera'
    ],
    'Engine_CC': [
        1497, 1197, 2199,  # Kia
        1997, 2184, 1997,  # Mahindra
        999, 1498, 1498,   # Volkswagen
        1496, 1996, 1194,  # Ford
        999, 1498,         # Nissan
        1451, 1349, 1996,  # MG
        999, 999, 1498,    # Renault
        1984, 1984, 1498,  # Skoda
        1956, 1956, 1998,  # Jeep
        1898, 2999,        # Isuzu
        0, 0, 0,           # Tesla
        1998, 2993, 1998,  # BMW
        1395, 1984, 2995,  # Audi
        1595, 1991, 2996,  # Mercedes
        1969, 1969, 1969,  # Volvo
        1984, 2995, 2981   # Porsche
    ],
    'Price': [
        1100000, 800000, 2500000,  # Kia
        2500000, 1600000, 1800000,  # Mahindra
        700000, 1300000, 1500000,   # Volkswagen
        800000, 3000000, 600000,    # Ford
        700000, 1000000,            # Nissan
        1400000, 1100000, 2800000,  # MG
        400000, 700000, 1300000,    # Renault
        2600000, 3200000, 1500000,  # Skoda
        2600000, 3300000, 6000000,  # Jeep
        1700000, 3500000,           # Isuzu
        5000000, 6000000, 12000000, # Tesla
        4300000, 8200000, 4500000,  # BMW
        3500000, 6000000, 8000000,  # Audi
        4100000, 6500000, 11000000, # Mercedes
        4500000, 6500000, 8500000,  # Volvo
        8300000, 12000000, 15000000 # Porsche
    ],
    'Fuel_Type': [
        'Petrol/Diesel', 'Petrol/Diesel', 'Diesel',  # Kia
        'Petrol/Diesel', 'Diesel', 'Diesel',         # Mahindra
        'Petrol', 'Petrol/Diesel', 'Petrol/Diesel',  # Volkswagen
        'Petrol/Diesel', 'Diesel', 'Petrol',         # Ford
        'Petrol/Diesel', 'Petrol/Diesel',            # Nissan
        'Petrol/Diesel', 'Petrol', 'Diesel',         # MG
        'Petrol', 'Petrol', 'Petrol/Diesel',         # Renault
        'Petrol', 'Petrol', 'Petrol/Diesel',         # Skoda
        'Diesel', 'Diesel', 'Petrol',                # Jeep
        'Diesel', 'Diesel',                          # Isuzu
        'Electric', 'Electric', 'Electric',          # Tesla
        'Petrol', 'Diesel', 'Petrol/Diesel',         # BMW
        'Petrol', 'Diesel', 'Diesel',                # Audi
        'Petrol', 'Diesel', 'Diesel',                # Mercedes
        'Petrol/Diesel', 'Petrol/Diesel', 'Petrol/Diesel',  # Volvo
        'Petrol', 'Petrol', 'Petrol'                 # Porsche
    ],
    'Transmission': [
        'Manual/Automatic', 'Manual/Automatic', 'Automatic',  # Kia
        'Manual/Automatic', 'Manual/Automatic', 'Manual/Automatic',  # Mahindra
        'Manual', 'Manual/Automatic', 'Manual/Automatic',    # Volkswagen
        'Manual/Automatic', 'Automatic', 'Manual',           # Ford
        'Manual/Automatic', 'Manual/Automatic',              # Nissan
        'Manual/Automatic', 'Manual/Automatic', 'Automatic', # MG
        'Manual', 'Manual/Automatic', 'Manual/Automatic',    # Renault
        'Automatic', 'Automatic', 'Manual/Automatic',        # Skoda
        'Manual/Automatic', 'Manual/Automatic', 'Automatic', # Jeep
        'Manual', 'Automatic',                               # Isuzu
        'Automatic', 'Automatic', 'Automatic',               # Tesla
        'Automatic', 'Automatic', 'Automatic',               # BMW
        'Automatic', 'Automatic', 'Automatic',               # Audi
        'Automatic', 'Automatic', 'Automatic',               # Mercedes
        'Automatic', 'Automatic', 'Automatic',               # Volvo
        'Automatic', 'Automatic', 'Automatic'                # Porsche
    ],
    'Quantity': [
        5, 3, 2,  # Kia
        4, 7, 6,  # Mahindra
        1, 2, 4,  # Volkswagen
        2, 1, 3,  # Ford
        6, 2,     # Nissan
        6, 4, 2,  # MG
        10, 5, 3, # Renault
        2, 1, 4,  # Skoda
        3, 2, 1,  # Jeep
        3, 2,     # Isuzu
        8, 7, 3,  # Tesla
        5, 4, 6,  # BMW
        2, 3, 1,  # Audi
        6, 5, 3,  # Mercedes
        7, 6, 4,  # Volvo
        3, 2, 1   # Porsche
    ]
}

df = pd.DataFrame(data)._append(pd.DataFrame(additional_data),ignore_index=True)
print(df.head(5))

