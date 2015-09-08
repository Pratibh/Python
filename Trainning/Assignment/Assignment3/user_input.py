__author__ = 'pratibh'


print("Store the stock information")
print("Type exit to close entering the data")
names=[]
price =[]
quantity=[]
type=[]

while True:
    item_name = raw_input("\nEnter a name\n")
    if item_name=="exit":
        break
    item_price = raw_input("Enter the price\n")
    if  item_price=="exit":
        break
    item_quantity = raw_input("Enter the quantity\n")
    if item_quantity=="exit":
        break
    item_type = raw_input("Enter the type of item\n")
    if item_type=="exit":
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

