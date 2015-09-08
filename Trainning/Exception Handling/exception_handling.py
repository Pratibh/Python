__author__ = 'pratibh'

def divide(num):
   try:
    print(100/num)
   except ZeroDivisionError as val:
       print "cannot divide by zero",val
divide(0)