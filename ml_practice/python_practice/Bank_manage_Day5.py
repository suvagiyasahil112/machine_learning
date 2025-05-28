
# Display dynamic car/bike details, with help of company_name, model_name, cc, engine, 

#  car = {
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

# make a dynamic bank transaction with deposit,withdrawal, balance, mention category





# name,account number , balance, (deposite,withdrawal ,branch,bank name , balance , category  of transaction(cash,atm,upi,checque) )
class Bob:

    def __init__(self, name, account_num, __balance):
        self.__balance =__balance
        self.name = name
        self.account_num = account_num

    def attributes(self, checkacc, method, amount, withdraw,checkname,responce2):
        self.withdraw = withdraw
        self.checkacc = checkacc
        self.method = method
        self.amount = amount
        self.checkname=checkname
        self.responce2=responce2

    def details(self):
        
        self.checkname = input("\nENTER ACCOUNT HOLDER'S NAME: ")
        self.checkacc = int(input("\nENTER ACCOUNT NUMBER: "))
        if self.checkacc == self.account_num and self.checkname == self.name:

            # print("\n                   ACCOUNT FOUND")
            self.process()
        else:

            print("\n                   ACCOUNT NOT FOUND\n")
            self.details()

    def deposit_cash(self):

        self.deposit = int(input("ENTER AMOUNT: "))
        print("\n                   YOUR BALANCE BEFORE DEPOSIT WAS:", self.__balance)
        self.__balance += self.deposit
        print("\n                   YOUR BALANCE AFTER DEPOSIT IS:", self.__balance)

    def check_bal(self):

        print('\n                   ACCOUNT BALANCE:\n')
        return self.__balance

    def withdrawal(self):

        self.amount = float(input("\nENTER AMOUNT: "))
        
        if self.amount>self.__balance:

            print("\n                   INSUFFICIENT BALANCE\n")

        else:    

            print("\n                   YOUR BALANCE BEFORE WITHDRAW WAS:", self.__balance)
            self.__balance -= self.amount
            print("\n                   YOUR BALANCE AFTER WITHDRAW IS:", self.__balance)
            if (self.responce2 == 1):
                    print('\n                   METHOD OF TRANSACTION WAS BANK\n')
            elif (self.responce2 == 2):
                    print('\n                   METHOD OF TRANSACTION WAS UPI\n')
            elif (self.responce2 == 3):
                    print('\n                   METHOD OF TRANSACTION WAS CHEQUE\n')
            elif (self.responce2 == 4):
                    print('\n                 METHOD OF TRANSACTION WAS NET BANKING\n')
            else :
                    print("\n                   ENTER VALID NUMBER\n")

                 

    def process(self):

        print("\n                   WELCOME TO BANK OF BARODA\n")
    
        self.method = int(input('''ENTER METHOD OF TRANSACTION:\n
                                    1:TO CHECK BALANCE \n
                                    2:TO WITHDRAW CASH \n
                                    3:TO DEPOSIT CASH \n
                                    '''))
        if (self.method == 1):
            print("BALANCE:", self.check_bal())
        elif (self.method == 3):
            self.deposit_cash()
        elif (self.method == 2):
            self.responce2 = int(input('''\n                   ENTER METHOD OF WITHDRAWAL:
                    \n                   1:TO REGISTER TRANSACTION VIA BANK
                    \n                   2:TO REGISTER TRANSACTION VIA UPI
                    \n                   3:TO REGISTER TRANSACTION THROUGH CHEQUE
                    \n                   4:TO REGISTER TRANSACTION VIA NET BANKING \n
                    '''))
            self.withdrawal()
        else :
             print("\nENTER VALID NUMBER\n")
                
                  


holder1 = Bob('sahil',123,0)
holder1.details()
while(1):
        
        if( holder1.details==0):
            break
        else:
            holder1.process()

