__author__ = 'pratibh'

names = []
price = []
quantity = []
type = []

print("Enter the operation you want to perform\n")
case = raw_input("Type Store to save new information and Search to view the saved data \n")
case.lower()
if case == "store":

    print("Store the stock information")
    print("Type exit to close entering the data")
    while True:
        item_name = raw_input("\nEnter a name\n")
        if item_name == "exit":
            break
        item_price = raw_input("Enter the price\n")
        if item_price == "exit":
            break
        item_quantity = raw_input("Enter the quantity\n")
        if item_quantity == "exit":
            break
        item_type = raw_input("Enter the type of item\n")
        if item_type == "exit":
            break
        names.append(item_name)
        price.append(item_price)
        quantity.append(item_quantity)
        type.append(item_type)
    fp=open("Information.txt","a+")
    fp.write(str(names))
    fp.write(str(price))
    fp.write(str(quantity))
    fp.write(str(type))
    fp.close()
elif case == "search":
    user_search = raw_input("Enter the Search Item\n")
    print filter(lambda x: user_search in x, names)
    fp=open("Information.txt","r")
    print(fp.readlines())
    fp.close()

else:
    print "Program exit!! Have a nice day"