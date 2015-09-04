__author__ = 'pratibh'


def testDefaultParams(var1 = "hello", var2 ="world"):
    print(var1+" "+var2)

testDefaultParams()
testDefaultParams("This","Test")
testDefaultParams("Testing")
testDefaultParams(var2 ="python")



def fun(arg1,*arg2):
    print(arg1)
    print(arg2)

fun(1,2,3,4,5,6,7,8,9)


