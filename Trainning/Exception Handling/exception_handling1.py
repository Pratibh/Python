__author__ = 'pratibh'

try:
    print int("deerwalk")
except ValueError as value:
    print "cannot print string value casted to string "
    print "error code: ",value
else:
    print "Success"
finally:
    print "This is the finally block"
