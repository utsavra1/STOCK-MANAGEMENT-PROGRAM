from read import readfile
from datetime import datetime

def purchase_laptop():
    purchase_laptop = []
    last_price = 0
    
    print("Thank you for buying")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    while True:
        try:
            phone = int(input("Enter your phone :"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid phone number.")
            continue
    while True:
        print("*******************************************************************************************************")
        print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
        print("*******************************************************************************************************")
        a = 1
        file = open("laptops.txt","r")
        for line in file:
            print(a, "\t" + line.replace(",","\t"))
            a =a+ 1
        print("*******************************************************************************************************")  
        file.close()
        print("\n")

        correct_id = int(input("Please Provide the ID of the product you want to buy:"))
        print("\n")

        #Valid ID

        while correct_id <= 0 or correct_id > len(readfile()):
            print("Please provide a valid laptops ID !!")
            print("\n")
            correct_id = int(input("Please Provide the ID of the laptops you want to buy:"))
        quantity_required = int(input("Please Provide the number of quantity of the laptops you want to buy:"))
        print("\n")
            

        #Valid Quantity

        mydict = readfile()
        taken_quantity = mydict[correct_id][3]
        while quantity_required <= 0 or quantity_required > int(taken_quantity):
            print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the laptops screen")
            print("\n")
            quantity_required = int(input("Please Provide the number of quantity of the laptops you want to buy: "))
        print("\n")

        #Update the text file

        mydict[correct_id][3] = int(mydict[correct_id][3]) + int(quantity_required)

        file = open("laptops.txt","w")

        for values in mydict.values():
            file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
            file.write("\n")
        file.close()

       
 # calculate price of selected laptop
        name_of_product = mydict[correct_id][0]
        users_quantity = quantity_required
        per_price = mydict[correct_id][2]
        price_of_item = mydict[correct_id][2].replace("$",'')
        last_price = int(price_of_item)*int(users_quantity)
        last_price = round(last_price, 2)

        # add selected laptop to purchase list and update total price
        purchase_laptop.append([name_of_product, users_quantity, price_of_item, last_price])
        last_price += last_price


        total = 0
        VAT = 0.13*(last_price)
        for i in purchase_laptop:
            total += int(i[3])
        last_price = last_price
        date_time = datetime.now()
        
        choice = input("Do you want to buy more? (Y/N): ")
        while choice.lower() not in ['y', 'n']:
            choice = input("Please enter a valid input (Y/N): ")
        if choice.lower() == 'n':
            break
     # calculate VAT based on total price
    last_price += last_price
    VAT = 0.13*last_price
    last_price += VAT       

    # print final bill with all purchased items
    print("\n")
    print("\t \t \t \t Utsav's laptops Shop")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9862414547 ")
    print("\n")
    print("****************************************************************************************")
    print("laptops Details: ")
    print("****************************************************************************************")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("****************************************************************************************")
    print("\n")
    print("Purchase Details are:")
    print("************************************************************************************************************")
    print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("************************************************************************************************************")
    for i in purchase_laptop:
        print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("************************************************************************************************************")

    print("Vat Amount:",  VAT)
    print("Grand Total:" + str(last_price))
    print("Note: Vat Amount added to grand total")
    
    return name,phone,date_time,purchase_laptop,VAT,last_price
        

def sale_laptop():
    
    sold_laptop = []
    total_price = 0
    
    print("Thank you for selling")
    print("\n")
    print("*********************************************************************")
    print("We will need your name and number to print bill")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    while True:
        try:
            phone = input("Enter your phone :")
            break
        except ValueError:
            print("Invalid input! Please enter a valid phone number.")
            continue
    #while loop to ask user if they want to buy more laptop or not
    while True:
        
        print("*********************************************************************************************************")
        print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
        print("*********************************************************************************************************")
        file = open("laptops.txt","r")
        a = 1
        for line in file:
            print(a, "\t" + line.replace(",","\t"))
            a =a+ 1
        print("*********************************************************************************************************")  
        file.close()
        print("\n")
    
        correct_id = int(input("Please Provide the ID of the product you want to sell:"))
        print("\n")

        #Valid ID

        while correct_id <= 0 or correct_id > len(readfile()):
            print("Please provide a valid laptop ID !!")
            print("\n")
            correct_id = int(input("Please Provide the ID of the laptop you want to sell:"))

        quantity_required = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
        print("\n")

        #Valid Quantity

        mydict = readfile()
        taken_quantity = mydict[correct_id][3]
        while quantity_required <= 0 or quantity_required > int(taken_quantity):
            print("Dear Admin, the quantity you are looking for is not available in our shop. Please look again in the laptop List")
            print("\n")
            quantity_required = int(input("Please Provide the number of quantity of the laptop you want to sell: "))
        print("\n")

        #Update the text file

        mydict[correct_id][3] = int(mydict[correct_id][3]) - int(quantity_required)

        file = open("laptops.txt","w")

        for values in mydict.values():
            file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
            file.write("\n")
        file.close()

        #getting user purchased items

        name_of_product = mydict[correct_id][0]
        users_quantity = quantity_required
        per_price = mydict[correct_id][2]
        price_of_item = mydict[correct_id][2].replace("$",'')
        last_price = int(price_of_item)*int(users_quantity)
        last_price = round(last_price, 2)

        sold_laptop.append([name_of_product, users_quantity, price_of_item, last_price])
        total_price += last_price

        choice = input("Do you want to sell more laptop ?(y/n):")
        print("\n")
        while choice.lower() not in ["y","n"]:
            choice = input("Please enter (y/n)!!:")
        if choice.lower() == "n":
            break
    
    date_time = datetime.now()
    shippingcost = input("Dear Customer do you want your laptops to be shipped?(Y/N)").lower()
    if shippingcost == "y":
        total = 0
        shippingcost = 500
        for i in sold_laptop:
            total = total + int(i[3])
        total_price = total_price + shippingcost           
        today_date_and_time = datetime.now()
        
        print("\n")
        print("\t \t \t \t  Utsav's laptop Shop")
        print("\n")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9862414547 ")
        print("****************************************************************************************")
        print("\n")
        print("Customer's Details: ")
        print("*****************")
        print("Customer Name:" + str(name))
        print("Phone Number: " + str(phone))
        print("Date and Time: " + str(date_time))
        print("****************************************************************************************")
        print("\n")
        print("Purchase Details are:")
        print("************************************************************************************************************")
        print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
        print("************************************************************************************************************")
        for i in sold_laptop:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("************************************************************************************************************")
        if shippingcost:
            print("Your total Price of laptop is: $"+str(total))
            print("Your Shipping Cost: $", shippingcost)
            print("Grand Total: $" + str(total_price))
            print("Note: Shipping Cost has been added to grand total")
        else:
            print("Grand Total: $" + str(total))
    else:
        total = 0
        shippingcost = 0
        for i in sold_laptop:
            total = total + int(i[3])
        total_price = total + shippingcost
        today_date_and_time = datetime.now

        print("\n")
        print("\t \t \t \t  Utsav's laptop Shop")
        print("\n")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9862414547 ")
        print("****************************************************************************************")
        print("\n")
        print("Customer's Details: ")
        print("*****************")
        print("Customer Name:" + str(name))
        print("Phone Number: " + str(phone))
        print("Date and Time: " + str(date_time))
        print("****************************************************************************************")
        print("\n")
        print("Purchase Details are:")
        print("************************************************************************************************************")
        print("Product Name \t\t Total Quantity \t\t Unit Price \t\t\t Total")
        print("************************************************************************************************************")
        for i in sold_laptop:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
        print("************************************************************************************************************")
        
        print("Your total Price is: $"+str(total))
        print("Your shipping cost is: $"+str(shippingcost))
        print("Grand Total: $"+str(total_price))
        print("Note: Shipping cost has not been added to the grand total")  
            
    return name,phone,date_time,sold_laptop,shippingcost,total_price,total
