a = {'code': 101, 'item': 'KitKat', 'price': 5} #Here are the indicated prices for each items 
b = {'code': 102, 'item': 'Skittles', 'price': 2.50}
c = {'code': 103, 'item': 'Twix', 'price': 3}
d = {'code': 104, 'item': 'Smarties', 'price': 1.50}
e = {'code': 105, 'item': 'Bubbly', 'price': 3}
f = {'code': 106, 'item': 'M&Ms', 'price': 4}
g = {'code': 107, 'item': 'Mars', 'price': 2}
h = {'code': 108, 'item': 'Snickers', 'price': 3}
i = {'code': 109, 'item': 'Dairy Milk', 'price': 10}
j = {'code': 110, 'item': 'Nescafe', 'price': 3.50}
k = {'code': 201, 'item': 'Water', 'price': 1}
l = {'code': 202, 'item': 'Apple Juice', 'price': 2}
m = {'code': 203, 'item': 'Oarnge Juice', 'price': 2}
n = {'code': 204, 'item': 'Tropical Juice', 'price':2}
o = {'code': 205, 'item': 'Perier Water', 'price': 8}
p = {'code': 206, 'item': 'Shani', 'price': 2.50}
q = {'code': 207, 'item': 'Red Bull', 'price': 5}
r = {'code': 208, 'item': 'Mountain', 'price': 2.50}
s = {'code': 209, 'item': 'Coke', 'price': 3}
t = {'code': 210, 'item': 'Sprite', 'price': 3}
items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t] #list of items
money = 0

 


print("╔══════════════════════╗")
print("║   VENDING MACHINE    ║")
print("╠══════════════════════╣")
print("║  [ ]  [ ]  [ ]  [ ]  ║")
print("║  [ ]  [ ]  [ ]  [ ]  ║")
print("║  [ ]  [ ]  [ ]  [ ]  ║")
print("║  [ ]  [ ]  [ ]  [ ]  ║")
print("╠══════════════════════╣")
print("║    ______________    ║")
print("║   |  COLLECT    |    ║")
print("║   |   HERE      |    ║")
print("╚══════════════════════╝")




KitKat = 5 #assigning prices in the products
Skittles = 2.50
Twix = 3
Smarties = 1.50
Bubbly = 3
MnM = 4
Mars = 2.50
Snickers = 3
Dairy_Milk = 10
Nescafe = 3.50
Water = 1
Apple_Juice = 2
Orange_Juice = 2
Tropical_Juice = 2
Perier_Water = 8
Shani = 2.50
Red_Bull = 5
Mountain_Dew = 3
Coke = 3
Sprite = 3

def show(items): #"show(items)" will print out the items that are available with their code and price when code is placed
    print('\nitems available \n')
    print("------------------------")
    for item in items:
        print(item.get('code'), item.get('item'), item.get('price'))

print("")
money = float(input("Input money: ")) #This is where the user inputs their choice of amount of money
PurchaseAgain = True #As a result, the code on "Purchase Again" is currently true.
while PurchaseAgain == True: #This will begin to go over again as a loop when the user starts the vending machine
    show(items) #Prints "show(items)"
    print("------------------------")
    print("")
    Item_selection = input("Input code: ") #This will let the user input their item of choice when inouting the code
    print("")

    if Item_selection == '101': #If the code 101 is purchase then it will play this path
        print("Item selected = KitKat | Price = 5 ") #This code will print the item and the price range of the item
        if money < KitKat: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds" 
            print("Insufficient Funds")
        elif money >= KitKat: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= KitKat #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour KitKat has been dispensed.") #This will print the money that was left after the purchase
            #This will show that the product that has been purchased has been dispense
        



    elif Item_selection == '102': #If the code 102 is purchase then it will play this path
        print("Item selected = Skittles | Price = 2.50 ") #This code will print the item and the price range of the item
        if money < Skittles: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Skittles: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Skittles #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Skittles has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            
    

    elif Item_selection == '103': #If the code 103 is purchase then it will play this path
        print("Item selected = Twix | Price = 3 ") #This code will print the item and the price range of the item
        if money < Twix: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Twix: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Twix #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Twix has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    elif Item_selection == '104': #If the code 104 is purchase then it will play this path
        print("Item selected = Smarties | Price = 1.50 ") #This code will print the item and the price range of the item
        if money < Smarties: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Smarties: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Smarties #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Smarties has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
        

    

    elif Item_selection == '105': #If the code 105 is purchase then it will play this path
        print("Item selected = Bubbly | Price = 3 ") #This code will print the item and the price range of the item
        if money < Bubbly: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Bubbly: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Bubbly #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Bubbly has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    elif Item_selection == '106': #If the code 106 is purchase then it will play this path
        print("Item selected = MnM | Price = 4 ") #This code will print the item and the price range of the item
        if money < MnM: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= MnM: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= MnM #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour MnM has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense


    


    elif Item_selection == '107': #If the code 107 is purchase then it will play this path
        print("Item selected = Mars | Price = 2.50 ") #This code will print the item and the price range of the item
        if money < Mars: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Mars: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Mars #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Mars has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    elif Item_selection == '108': #If the code 108 is purchase then it will play this path
        print("Item selected = Snickers | Price = 3 ") #This code will print the item and the price range of the item
        if money < Snickers: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Snickers: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Snickers #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Snickers has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            

    

    elif Item_selection == '109': #If the code 109 is purchase then it will play this path
        print("Item selected = Dairy Milk | Price = 10 ") #This code will print the item and the price range of the item
        if money < Dairy_Milk: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Dairy_Milk: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Dairy_Milk #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Dairy Milk has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense



    elif Item_selection == '210': #If the code 210 is purchase then it will play this path
        print("Item selected = Nescafe | Price = 10 ") #This code will print the item and the price range of the item
        if money < Nescafe: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Nescafe: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Nescafe #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Nescafe has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            


    

    elif Item_selection == '201': #If the code 201 is purchase then it will play this path
        print("Item selected = Water | Price = 1 ") #This code will print the item and the price range of the item
        if money < Water: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Water: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Water #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Water has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    elif Item_selection == '202': #If the code 202 is purchase then it will play this path
        print("Item selected = Apple Juice | Price = 2 ") #This code will print the item and the price range of the item
        if money < Apple_Juice: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Apple_Juice: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Apple_Juice #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Apple_Juice has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    

    elif Item_selection == '203': #If the code 203 is purchase then it will play this path
        print("Item selected = Orange Juice | Price = 2 ") #This code will print the item and the price range of the item
        if money < Orange_Juice: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Orange_Juice: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Orange_Juice #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Orange Juice has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            


    

    elif Item_selection == '204': #If the code 204 is purchase then it will play this path
        print("Item selected = Tropical Juice | Price = 2 ") #This code will print the item and the price range of the item
        if money < Tropical_Juice: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Tropical_Juice: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Tropical_Juice #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Tropical Juice has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    
    elif Item_selection == '205': #If the code 205 is purchase then it will play this path
        print("Item selected = Perier Water | Price = 8 ") #This code will print the item and the price range of the item
        if money < Perier_Water: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Perier_Water: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Perier_Water #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Perier Water has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
    





    elif Item_selection == '206': #If the code 206 is purchase then it will play this path
        print("Item selected = Shani | Price = 2.50 ") #This code will print the item and the price range of the item
        if money < Shani: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Shani: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Shani #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Shani has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
     




    elif Item_selection == '207': #If the code 207 is purchase then it will play this path
        print("Item selected = Red Bull | Price = 5 ") #This code will print the item and the price range of the item
        if money < Red_Bull: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Red_Bull: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Red_Bull #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Red Bull has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense




    elif Item_selection == '208': #If the code 208 is purchase then it will play this path
        print("Item selected = Mountain Dew | Price = 3 ") #This code will print the item and the price range of the item
        if money < Mountain_Dew: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Mountain_Dew: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Mountain_Dew #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Mountain Dew has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            


    
    elif Item_selection == '209': #If the code 209 is purchase then it will play this path
        print("Item selected = Coke | Price = 3 ") #This code will print the item and the price range of the item
        if money < Coke: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Coke: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Coke #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Coke has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense





    elif Item_selection == '210': #If the code 210 is purchase then it will play this path
        print("Item selected = Sprite | Price = 3 ") #This code will print the item and the price range of the item
        if money < Sprite: #When there is not enough money to purchase the selected item, the code will appear with "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Sprite: #If the user's money is equal or more than the amount of the item, then the selected iteme of the user will continue
            money -= Sprite #Here is where the machine will give change to the amount you have inserted from the selected product
            print('Change returned: ' + str(money) + "\nYour Sprite has been dispensed.") #This will print the money that was left after the purchase
        #This will show that the product that has been purchased has been dispense
            



    else: #if the code that the user inputted is not one of the product's codes, it will print "Invalid code"
        print("Invalid code")

    choice = input('Buy something else? (y/n): ') #this code gives the user the choice of if they want to purchase another item or not
    if choice == 'n': #if the user inputs "n" it goes through this path
        PurchaseAgain = False #the loop stops

        if money != 0: #if money is not equal to 0, the code goes through this path
            print(str(money) + ' money left') #this prints the amount of money the user has left
            money = 0 #this makes the amount of money return to zero
            print('Thank you for buying, come again soon!\n')
            break
        else: #if money is equal to 0, the code just prints the final message
            print('Thank you for buying, come again soon!\n')
            break
    else: #if the user inputs "y" the code loops back to "PurchaseAgain"
        continue

    

   


           



            

        


    
        
