
username_pass={'1':'123','2':'355','3':'654','4':'546','5':'876','6':'698'}


inp1=(input('enter username:'))
inp2=input('enter password:')
# username_pass['7']='856'



if inp1 in username_pass and username_pass[inp1]==inp2:
    print('login sucessfully.')     
elif inp1 not in username_pass :
    print("incorrect username")
elif inp1 in username_pass and username_pass[inp1]!=inp2:
    print ('incorrect password')    
else:
    print("inncorrect both username and password")    

   


