__author__ = 'pratibh'

def fun(li):
    li.append("a")
    print "from method:",li


li1 =[1,2,3]
print "before:",li1
fun(li1)
print"after:",li1
