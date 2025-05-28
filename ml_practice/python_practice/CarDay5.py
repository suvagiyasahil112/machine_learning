
# # Display dynamic car/bike details, with help of company_name, model_name, cc, engine, 
# # Cars grouped by company using lists

class Car:
    def __init__(self,name,engine_cc,price,fuel_type,transmission,quantity):
        self.name=name
        self.engine_cc=engine_cc
        self.price=price
        self.fuel_type=fuel_type
        self.transmission= transmission
        self.quantity=quantity

    def __str__(self):
          return(f"{self.name} - Engine: {self.engine_cc}cc, Price: ₹{self.price}, "
                    f"Fuel: {self.fuel_type}, Transmission: {self.transmission} ,QUANTITY: {self.quantity}")

class Company(Car):
     
    def __init__(self,name):
        self.name=name
        self.cars=[]
    def add_car(self,car):
        self.cars.append(car)

    def del_car (self,car):
        self.cars.pop(car)
   

    def __str__(self):
            result = f"{self.name}:\n"
            result+="\n".join([f"{car}" for car in self.cars])
            return result
    
    # def admin(self,name,password):
    #     self.name=name
    #     self.password=password
    #     pass
    
companies=[]
maruti = Company("Maruti Suzuki")
maruti.add_car(Car("Swift", 1197, 750000, "Petrol/Diesel", "Manual/Automatic",0))
maruti.add_car(Car("Baleno", 1197, 650000, "Petrol", "Manual/Automatic",1))
maruti.add_car(Car("Dzire", 1197, 850000, "Petrol", "Manual/Automatic",3))

# Hyundai
hyundai = Company("Hyundai")
hyundai.add_car(Car("Creta", 1497, 1350000, "Petrol/Diesel", "Manual/Automatic",4))
hyundai.add_car(Car("Venue", 1197, 800000, "Petrol/Diesel", "Manual/Automatic",6))
hyundai.add_car(Car("Verna", 1497, 1200000, "Petrol/Diesel", "Manual/Automatic",2))

# Tata Motors
tata = Company("Tata Motors")
tata.add_car(Car("Nexon", 1199, 950000, "Petrol/Diesel", "Manual/Automatic",0))
tata.add_car(Car("3", 1956, 1500000, "Diesel", "Manual/Automatic",2))
tata.add_car(Car("Altroz", 1199, 630000, "Petrol/Diesel", "Manual",2))

toyota =Company("Toyota")  # Company Name
toyota.add_car(Car("Fortuner", 2755, 4000000, "Diesel", "Automatic",3))
toyota.add_car(Car("Innova Crysta", 2393, 2000000, "Diesel", "Manual/Automatic",5))
       

honda =  Company("Honda")
honda.add_car(Car("Amaze", 1199, 800000, "Petrol", "Manual/Automatic",2))
honda.add_car(Car("City", 1498, 1300000, "Petrol/Diesel", "Manual/Automatic",3))

companies.append(maruti)
companies.append(hyundai)
companies.append(tata)
companies.append(toyota)
companies.append(honda)


# car1=Car('c',3,4,'tt','oo')
# print(car1.__str__())

# for company in companies:

#      print("\n",company)

# records=[["0 sahil 10 Fortuner"],["1 kk 90 Toyota"]]
# # print(records[0])
# for i in records:
#     print(i)


while(1):
    print ("\nwelcome to car dealers")
    inp=int (input(('''\n ENTER 1 FOR SHOW ALL CARS\n ENTER 2 FOR SHOW ALL CARS FROM SPECIFIC COMPANY\n ENTER 3 TO FILTER CARS BY PRICE\n ENTER 4 ADD A NEW CAR\n ENTER 5 TO BUY A CAR \n ENTER 9 TO EXIT ''')))

    if inp==1:
        for company in companies:
            print("\n",company)
    elif inp==2:
        company_name=input("\nENTER NAME OF COMPANY:")
        for company in companies:
            if company.name == company_name: 
                print(f"\n CARS FROM {company_name}:")
                print(company)
                break
            else:
                continue
                print(f"NO COMPANY FOUND FOR {company_name}")   
    elif inp==9:
        break

    elif inp==3:
        try:
            responce3min=int(input('''\nENTER STARTING POINT OF PRICE RANGE'''))
            responce3max=int(input('''\nENTER ENDING POINT OF PRICE RANGE\n'''))
            
            
            foundcars=False
            for company in companies:
                print(company.name)
                for car in company.cars:
                    if  responce3min <=car.price<= responce3max>=car.price :
                        print("\n",car.__str__())
                        foundcars=True
            if not foundcars:
                print('NO CARS AVAILABLE IN PRICE RANGE') 

        except ValueError :
            print("PLEASE ENTER INTEGER NUMBER FOR RANGE")   

    elif inp==4:
        company_name=input("ENTER COPANY NAME FOR NEW CAR:")
        for company in companies:
            if company.name==company_name:
                car_name=input('ENTER NEW CAR NAME:')
                engine_cc=int(input('ENTER NEW CAR ENGINE CC:'))
                price=int(input('ENTER NEW CAR PRICE:'))
                fuel_type=input('ENTER NEW CAR FUEL TYPE:')
                transmission=input('ENTER NEW CAR TRANSMISSION:')
                quantity=int(input('ENTER NEW CAR QUANTITY:'))
                new_car=Car(car_name,engine_cc,price,fuel_type,transmission,quantity)
                check=False
                for car in company.cars: 
                    for company in companies:   
                    
                        if( car_name==car.name
                            and engine_cc==car.engine_cc 
                            and price==car.price 
                            and fuel_type==car.fuel_type 
                            and transmission==car.transmission):
                            check=True
                            car.quantity+=quantity
                            print("SUCESSFULLY ADDDED TO INVENTORY")
                            break
                        

                        elif check== False:
                            company.add_car(new_car)
                            print(f"NEW CAR {car_name} ADDED TO COMPANY {company_name} SUCESSFULLY!")
                            break

                        else:
                            break
            else :
                print(f"COMPANY {company_name} NOT FOUND PLEASE TRY AGAIN")


    elif inp==5:
        company_name=input("ENTER COPANY NAME TO BUY CAR:")
        for company in companies:
            if company.name==company_name:
                car_name=input('ENTER CAR  NAME:')
                engine_cc=int(input('ENTER CAR ENGINE CC:'))
                price=int(input('ENTER  CAR PRICE:'))
                fuel_type=input('ENTER CAR FUEL TYPE:')
                transmission=input('ENTER  CAR TRANSMISSION:')
                quantity=int(input('ENTER  CAR QUANTITY:'))
                new_car=Car(car_name,engine_cc,price,fuel_type,transmission,quantity)
                check=False
                for car in company.cars: 
                    for company in companies:   
                    
                        if( car_name==car.name
                            and engine_cc==car.engine_cc 
                            and price==car.price 
                            and fuel_type==car.fuel_type 
                            and transmission==car.transmission):
                            check=True
                            if quantity<1:
                                print("PLEASE ENTER POSITIVE AND NUMBER GREATER THAN 0")
                            elif car.quantity<quantity:
                                print(f"{car.quantity} CARS AVILABLE")
                            else:
                                car.quantity-=quantity
                                print(f"SUCESSFULLY BOUGHT CAR",car.__str__())
                                break
                        # {car_name} COMPANY :{company_name}
                        

                        elif check== False:
                            company.del_car(new_car)
                            print(f"NEW CAR {car_name} COMPANY {company_name} BOUGHT SUCESSFULLY!")
                            break

                        else:
                            break
            else :
                pass
                # print(f"COMPANY {company_name} NOT FOUND PLEASE TRY AGAIN")


    else :
        print("\nENTER VALID INPUT")    



