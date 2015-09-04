__author__ = 'pratibh'

list1 = [1,2,3,4,5,6,6,7,8,9,9,10]

# returns odd number
# x%2 gives result 0. in filter only true value is returned. We have assumed 0 as a false value
result = filter(lambda x:x%2,list1)
print result

# returns even numbers
result = filter(lambda x:x%2==0,list1)
print result

def  fil(a):
    return a%2

print "output:",filter(fil,list1)

