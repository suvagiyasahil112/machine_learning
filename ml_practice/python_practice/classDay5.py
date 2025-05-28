
class name:
    def __init__(self,name,surname,age):
        self.name=name
        self.surnname=surname
        self.age=age
    
    def greet(self):
        # self.age=00
        # self.name='sss'
        # self.surnname='oio'
        print('hello,',self.surnname,self.name,", are you 00 year old?")


name1 = name("sahil",'suvagiya', 25)  
name1.greet()    






















# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
                
#     def display(self):
#         print(self.modelname,self.year)
        
# c1=car('abc',1232)
# c2=car('jjl', 1718)


# class toyota(car) :
#     def __init__(self,engine):
#         self.engine=engine

#     def printing():
#         print('accecing attribute from car class:',c1.modelname,c1.year)    

# toyota.printing()


# c1=car("toyota",2019)
# c2=car("bently",2010)
# c3=car("mercedes",2018)

# c1.display()
# c2.display()
# c3.display()