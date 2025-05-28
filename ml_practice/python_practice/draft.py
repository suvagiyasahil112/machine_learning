import random
import pandas as pd

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

df= pd.DataFrame(data)._append(pd.DataFrame(additional_data),ignore_index=True)
count_of_row_lebels=len(df.index)
print(count_of_row_lebels)

print(df)
try:   
    while(1):
        print ("\nwelcome to car dealers")
        inp=int(input(('''\n ENTER 1 FOR SHOW ALL CARS\n ENTER 2 FOR SHOW ALL CARS FROM SPECIFIC COMPANY\n ENTER 3 TO FILTER CARS BY PRICE\n ENTER 4 ADD A NEW CAR\n ENTER 5 TO BUY A CAR \n ENTER 9 TO EXIT \n RESPONSE:''')))

        if inp==1:
            print(df)
            
        elif inp==2:
            company_name=str(input("\nENTER NAME OF COMPANY:"))
            
            
            print(df.loc[df['Company'] == company_name])
    
        elif inp==9:
            break

        elif inp==3:
            try:
                responce3min=int(input('''\nENTER STARTING POINT OF PRICE RANGE'''))
                responce3max=int(input('''\nENTER ENDING POINT OF PRICE RANGE\n'''))
            
                foundcars=False
                for key in  data.keys():
                    if key=="Price":
                        
                        
                        y=list(data.values())
                        
                        val=y[3]
                        
                        filtered_car_price=[]
                        

                        for b in val:
                            if responce3max>=b>=responce3min:
                                print(b)
                                filtered_car_price.append(b)
                                for d in filtered_car_price :
                                    car_price_rupee=d
                                    row_label = not list
                                    row_label = df.loc[df['Price'] == car_price_rupee]
                                
                                    print(row_label,"\n\n\n")
                                    foundcars=True  
                if not foundcars:
                    print('NO CARS AVAILABLE IN PRICE RANGE') 

            except ValueError :
                print("PLEASE ENTER INTEGER NUMBER FOR RANGE")   

        elif inp==4:
                company_name=input("ENTER COPANY NAME OF COMPANY:")
                car_name=str(input('ENTER CAR  NAME:'))
                engine_cc=int(input('ENTER CAR ENGINE CC:'))
                price=int(input('ENTER  CAR PRICE:'))
                fuel_type=input('ENTER CAR FUEL TYPE:')
                transmission=input('ENTER  CAR TRANSMISSION:')
                quantity=int(input('ENTER  CAR QUANTITY:'))
                templist=[]
                templist=[company_name,car_name,engine_cc,price,fuel_type,transmission,quantity]

                if ( 
                    templist[0] in list(df['Company'])and
                    templist[2] in list(df['Engine_CC'])and
                    templist[1] in list(df['Name'])and
                    templist[3] in list(df['Price']) and
                    templist[4] in list(df['Fuel_Type']) and
                    templist[5] in list(df['Transmission'])

                    ):
                    for i in list(df['Name']):
                        if i==templist[1]:
                            # print(i)
                            pass
                            
                    
                    
                    a= df.at[df.loc[df['Name']==car_name].index[0], 'Quantity']
                    
                    index_of_that_car=df.loc[df['Name']==i].index[0]
                
                    a= df.at[df.loc[df['Name']==car_name].index[0], 'Quantity']
                    b=templist[6]
                    c=a+b
                    templist[6]=c
                    df.loc[index_of_that_car]=templist
                    print(df)

                
                else:    
                    df.loc[count_of_row_lebels]=templist
                    count_of_row_lebels+=1
                    print(df)

        elif inp==5:
                company_name=input("ENTER COPANY NAME OF COMPANY TO BUY A CAR:")
                car_name=str(input('ENTER CAR  NAME :'))
                engine_cc=int(input('ENTER CAR ENGINE CC:'))
                price=int(input('ENTER  CAR PRICE:'))
                fuel_type=input('ENTER CAR FUEL TYPE:')
                transmission=input('ENTER  CAR TRANSMISSION:')
                quantity=int(input('ENTER  CAR QUANTITY:'))
                templist=[]
                templist=[company_name,car_name,engine_cc,price,fuel_type,transmission,quantity]
                check=False


                if ( 
                    templist[0] in list(df['Company'])and
                    templist[2] in list(df['Engine_CC'])and
                    templist[1] in list(df['Name'])and
                    templist[3] in list(df['Price']) and
                    templist[4] in list(df['Fuel_Type']) and
                    templist[5] in list(df['Transmission'])

                    ):
                    check=True
                    if quantity<1:
                        print("PLEASE ENTER POSITIVE AND NUMBER GREATER THAN 0")
                    elif df.at[df.loc[df['Name']==car_name].index[0], 'Quantity']<quantity:
                        print(f"{ df.at[df.loc[df['Name']==car_name].index[0], 'Quantity']} CARS AVILABLE")
                    else:
                        df.at[df.loc[df['Name']==car_name].index[0], 'Quantity']-=quantity
                        print(f"SUCESSFULLY BOUGHT CAR")
                else:    
                    print("CAR IS NOT AVAILABLE")
                    print(df)
        else :
            print("\nENTER VALID INPUT")    
except ValueError as val:
    print("ENTER VALID INPUT")
 