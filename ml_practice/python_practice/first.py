# print("hello.....")

# x = "sahil"

# print(x)

# print("hello, ",x)

# name = input("Enter your name : ")
# print("your name is ",name)

# data- types

# 1. list methods - [] , change , duplicate , indexing

# list_ex = ['list1','list2','list3','list1']

# x = list[1]
# print(x)

# list_ex.append('list4')
# list_ex.insert(1,'list5')

# list_ex.remove('list1')
# list_ex.pop(1)

# list_ex[1] = "list7"

# x = len(list_ex)
# print(x)

# y = list_ex.count('list2')
# print(y)

# list_ex.clear()

# print(list_ex)


# 2. tuple methods - () , not change , duplicate , indexing

# tup = ('tup1','tup2','tup3')

# ab = list(tup)
# print(type(ab))


# tup = tuple(ab)
# print(type(tup))


# 3. set methods - {} , change , no duplicate , no indexing

# st = {'set1','set2','set3'}

# st.add('set4')

# st.pop()
# st.remove('set1')

# print(st)


# 4. dictionary methods - {} , change , duplicate(value) , indexing(key)

# dit = {
#     'car':'mercedes',
#     'bike':'yamaha',
#     'scooty':'pept',
#     }

# x = dit['car']
# print(x)

# dit['truck'] = 'Eicher'

# dit.popitem()
# dit.pop('car')

# x = dit.keys()
# print(x)
# y = dit.values()
# print(y)

# print(dit)


# conditional statement 

# if else

# x = 5

# if x > 50 :
#     print("big")
# else:
#     print("small")

# nested if else 

# x = 17

# if x>10:
#     print("big than 10")
#     if x>20:
#         print("big than 20")
#         if x>30:
#             print("big than 30")
#         else:
#             print("small than 30")
#     else:
#         print("small than 20")
# else:
#     print("small than 10")


# loops 

# for loop 

# x = [45,45,4,556,57]


# for a in range(45,56):
#     if a>50:
#         print("big",a)
#     else:
#         print("small",a)



# while loop 

# i=0
# while i<11:
#     print(i)
#     i=i+1


# take user input, check username and password whether user can login or not

# take user input and print table(7 * 1 = 7) using both loops 

# make dynamic calculator

# take user input as age and check whether user can vote or not and is senior citizen or not

# functions  
# name = input("Enter name : ")

# def myfunc(name):
#     print("helooo",name)

# myfunc(name)

# print("hiiiiiiiii")
# print("heyyyaaa")


# try- except 


# print("before code")
# # x = 45
# try:
#     print(x)
# except Exception as e:
#     print("error",e)

# print("after code")


# dynamic marksheet

# convert all codes to function based codes

# while using functions, make sure to use parameters


# OOPs concepts 

# polymorphism
# inheritance
# encapsulation


# class Car:
#     engine = "250cc"
#     tyre = "JK"

#     def start_car():
#         print("car starting")


# xyz = Car
# xyz.start_car()


# polymorphism

# class Phone:
#     def sound(self):
#         pass

# class Sahil:
#     def sound(self):
#         return "dream"

# class HJ:
#     def sound(self):
#         return "alone"

# sahil = Sahil()
# print(sahil.sound())

# hj = HJ()
# print(hj.sound())


# Inheritance 

# class Animal:
#     def eat_all(self):
#         print("animals eat to survive")


# class herbi(Animal):
#     def eat(self):
#         print("They only plants")

# class Carni(Animal):
#     def eat(self):
#         print("They only eat meat")


# hb = herbi()
# hb.eat()
# hb.eat_all()

# car = Carni()
# car.eat()
# car.eat_all()


# class Bank():
#     def __init__(self,balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self,amount):
#         print("before balance",self.__balance)
#         print("amount",amount)
#         self.__balance += amount
#         print("after balance",self.__balance)
#         return amount

# acc = Bank(1000)
# acc.deposit(500)
# print("reeteg",acc.get_balance())

# print(acc.__balance) 



# make a dynamic bank transaction with deposit,withdrawal, balance, mention category
# car = {
#     1:{
#         'company_name':"mercedes",
#         'model_name':"mercedes",
#         'model_name':"mercedes",
#     },
#     2:{
#         'company_name':"bmw",
#         'model_name':"mercedes",
#         'model_name':"mercedes",
#     },

# }



# Display dynamic car/bike details, with help of company_name, model_name, cc, engine, 



# run 
#  options - add, show detail price , buy , 
# 1. add - car_name, company_name, 
# 2. search - car,company names  - show details = price(pet,dies,ele) + tax ,engine, no_of_cars
# 3. buy - enter car name , client name


# random 
# import random

# x = random.randint(100,999)
# print(x)

# y = random.randrange(1,10,3)   # 1,4,7
# print(y)


# from a deck of cards fetch 3 cards find probability of belows:
# 1. find that card is a face card
# 2. find 2 cards to be an ace card
# 3. find that all cards are multiple of 2

    


# import random
# rows=3
# cols=3
# zero="|O "
# eks="|X "
# tic = []
# def board(cols,rows):
#     for row in range(rows):
#         print("|  " * cols)
#         tic.append("| "*cols)

#     print("tic ",tic)

#     turn = 0
#     while (turn<=9):
#         if turn%2 != 0:
#             for row in range (rows*cols):
#                 if row== [random.randrange(0,3)][random.randrange(0,1)]:                
#                     print("|O |  | "   )
#                     continue   
#                 print("|  " * cols, )
#             print("\n \n ")
#             turn+=1 
#         if turn==0 or 2 or 4 or 6 or 8 :
#             for row in range(rows):
#                 if  row=="|  ":
#                     print("X")
#             print("\n \n ")
#             turn+=1   
       
    
# board(cols,rows)


# ------------------------------------- PANDAS ---------------------------
# import pandas as pd
# import numpy as np


# data = {
#     'name':['sahil','hj','khushi'],
#     'age':[34,4,54],
#     'value':[64,75,46]
# }

# df = pd.DataFrame(data)

# sr = pd.Series(data)



# print(df)
# print(sr)

# fetching
# age = df.iloc[1]
# print(age)


# first = df.head(2)

# last = df.tail(1)

# info = df.info()

# print(first)
# print(last)
# print(info)


# add/update column in df
# df['value'] = [4000,50000,400]

# rename df 
# df.rename(columns={'age':'gender'},inplace=True)

# df.pop('value')

# print(df)




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

df= pd.DataFrame(data)._append(pd.DataFrame(additional_data),ignore_index=True)


# print(df)
import matplotlib.pyplot as plt

import seaborn as sns 
plt.figure(figsize=(8,5))
plt.bar(df["Company"],df["Price"],color="skyblue")
plt.title("price by car")
plt.xlaabel= ("car")
plt.ylabel= ("price")
plt.grid=(True)
plt.show()

# for i  in df.iterrows():
#     print(i)
#     print()


# columns=list(df)

# print(type(columns))

# for i in columns:

#     print(df[i][2])

# least5 = data.nsmallest(5, "Salary")
# df.dropna(inplace=True)
# least5=data.nsmallest(5,"Price")
# least5

# extracting least 5
# cheapest5 = df.nsmallest(5, "Price")
# expensive5 = df.nlargest(5, "Price")
 
# display
# print(cheapest5)
# print()
# print(expensive5)
# print(df.head(3))
# print(df[:10])




