print("\t\t\tWelcome to HEMA RESTAURANT")
print('*'*80)
print("choose your food type:\n\t1.breakfast\n\t2.lunch\n\t3.dinner")
food_type=input("enter your food type: ").lower()
if food_type=='lunch':
   print("\tMenu\n",'*'*30,"\n1.CHICKEN BIRIYANI\n2.VEG MEALS\n3.SAMBAR RICE\n4.CURD RICE\n5.MUTTON BIRIYANI")
elif food_type=='breakfast':
    print("\tMenu\n",'*'*30,"\n1.DOSA\n2.IDLI\n3.UPMA\n4.PONGAL\n5.VADA")
elif food_type=='dinner':
    print("\tMenu\n",'*'*30,"\n1.CHICKEN FRIED RICE\n2.VEG BIRIYANI\n3.PAROTA\n4.PUTTU\n5.IDIYAPPAM")
item=input("enter your item:").lower()
if food_type=="breakfast":
    if item=="DOSA".lower():
        qty=int(input("enter the quantity: "))
        amt=20
    elif item=="IDLI".lower():
        qty=int(input("enter the quantity: "))
        amt=15
    elif item=="UPMA".lower():
        qty=int(input("enter the quantity: "))
        amt=25
    elif item=="PONGAL".lower():
        qty=int(input("enter the quantity: "))
        amt=15
    elif item=="VADA".lower():
        qty=int(input("enter the quantity: "))
        amt=7
elif food_type=="lunch":
    if item=="CHICKEN BIRIYANI".lower():
        qty=int(input("enter the quantity: "))
        amt=250
    elif item=="VEG MEALS".lower():
        qty=int(input("enter the quantity: "))
        amt=100
    elif item=="SAMBAR RICE".lower():
        qty=int(input("enter the quantity: "))
        amt=20
    elif item=="CURD RICE".lower():
        qty=int(input("enter the quantity: "))
        amt=50
    elif item=="MUTTON BIRIYANI".lower():
        qty=int(input("enter the quantity: "))
        amt=200
elif food_type=="dinner":
    if item=="CHICKEN FRIED RICE".lower():
        qty=int(input("enter the quantity: "))
        amt=120
    elif item=="VEG BIRIYANI".lower():
        qty=int(input("enter the quantity: "))
        amt=100
    elif item=="PAROTA".lower():
        qty=int(input("enter the quantity: "))
        amt=20
    elif item=="PUTTU".lower():
        qty=int(input("enter the quantity: "))
        amt=25
    elif item=="IDIYAPPAM".lower():
        qty=int(input("enter the quantity: "))
        amt=10
print("\tRECEIPT\n",'*'*30,"\nITEM =",item,"\nQUANTITY =",qty,"\nPRICE=",amt,"RS","\nAMOUNT =",amt*qty,"RS")    
        
             
    
