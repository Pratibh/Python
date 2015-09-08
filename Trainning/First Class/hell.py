#!/usr/bin/python

print("This is test")

ram = "test product test"
print(ram)	
a = 1 
b = 3 

if a>b:
	print("a is greater")

else:
	print("b is greater")

print type(a)
print(a)
a="test"
print type(a)
print(a)

test_single ='ram'
test_double ="hari"
test_triple="""Hari"""

test_triple="""this is test_triple
	bla bla bla """


num1 = 10
num2 = 20.00

print("%f is a float and %d is an integer" %(num2,num1))

float_num = 1.23456
print("%.2f" %(float_num))

concat = 12.00
print("%d" %(concat))
print("1%d" %(concat))
print("%-d" %(concat))
print("%20d" %(concat))



name ="ramisa goodboy"
a = 2*3
print(name[0])
print len(name)
print name[0:3]
print name[0:4]
print name[:5]
print name[6:] 
print name[-5:-1]
print name[-4:-1]
print name * 2
print name +'!!'
print name[1:5] *a

_values =[12234,"abchefjs","ram", 1.222]
print(_values)
print len(_values)

_values.sort()
print("Sorted values" )
print(_values)

_values.reverse()
print("Reversed values")
print(_values)

# print dir(name)

# Extend
names =["ram","shyam","hari"]
rollno =[1,2,3]

# inserts as a  part of the list 
names.extend(rollno)

print(names)

# considers as a object
names.append(rollno)
print(names) 

# Append
names1=["arun", "anil"]
test ="ham"
names1.append(test)
print(names1)

list_one=["ram"]
list_one.extend("hello")
print(list_one)
list_one.extend(["hello"])
print(list_one)

# Multidimensional Array

list_array =[[1,2],["ram","hari"]]
print(list_array[1])
print(list_array[1][1])


list_slice =[["a","b","c"],[1,2,3],[1,2,"c"]]
print(list_slice)

print(list_slice[-1])

# list_slice[2][0]="a"
# list_slice[2][1]="b"
# list_slice[2][2]="c"
# print(list_slice)

list_slice[2] = list_slice[0]
print(list_slice)

list_slice[2][0:2]=["x","y"]
print(list_slice)


tuple_test = (1,2,3,"ram")
print(tuple_test)
print tuple_test.count(1)

t1=(1,2)
t2=(3,4)
print cmp(t1,t2)

# list1 = [1,2,3]
# tuple1(list1)
# print (tuple1)

dic={}
print dir(dic)

dic={1:"arun",2:"pratibh",3:"sameer"}
print dic
print dic.keys()
print dic.values()

dic_country={"nepal":"kathmandu", "USA":"Delhi"}
print dic_country

dic_country["USA"]="washington"
print dic_country

dic_tuple = {"boys":["ram","shyam","hari"],"girls":["sita","gita"]}
print dic_tuple


# Try Delete and Clear
dic_tuple.pop("girls")
print dic_tuple

print dic_tuple.has_key("boys")

print dic_tuple.items()

dictionary = {1:"ram",2:"shyam"}
dictionary.setdefault(3,"hari")
print dictionary