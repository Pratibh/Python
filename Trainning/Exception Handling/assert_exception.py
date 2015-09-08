__author__ = 'pratibh'

def compare(a,b):
    try:
        assert (a==b),"%d is not equal to %d"%(a,b)
        print "True"
    except AssertionError as error:
        print error
compare(4,5)