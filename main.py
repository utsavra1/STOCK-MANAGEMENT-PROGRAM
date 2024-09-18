from operation import purchase_laptop
from operation import sale_laptop
from write import write_purchase, write_sales


print('\n')
print('------------------------------------------------------------------------')
print('\t \t \t Welcome to C1 ')
print('------------------------------------------------------------------------')
print('\t \t Address: BSL Contact: 9876543')
print('------------------------------------------------------------------------')
print('\n')

continueLoop = True
while continueLoop == True:

    print('\n')
    print('Press 1 to buy from manufacturer')
    print('Press 2 to sell to customer')
    print('Press 3 to exit')
    print('\n')
    print('------------------------------------------------------------------------')

    try:
        userinput = int(input('Press 1,2 or 3 :' ))

        #if 1 is pressed call write_purchase function
        if  userinput == 1:
            name,phone,date_time,purchase_laptop,VAT, total_price = purchase_laptop()
            write_purchase(name,phone,date_time,purchase_laptop,VAT,total_price)

        #if 2 is pressed call write_sales function
        elif userinput == 2:
            name,phone,date_time,sold_laptop, shippingcost,total_price, total = sale_laptop()
            write_sales(name,phone,date_time,sold_laptop,shippingcost,total_price,total)

        #if 3 is pressed exit loop
        elif userinput ==3:
            continueLoop = False
            print('Thank you for visiting')
        else:
            print('Enter correct option')
    except ValueError:
        print("incorrect value")
