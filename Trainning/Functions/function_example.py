__author__ = 'pratibh'

def fahrenheit(T):
    return ((float(9)/5)*T +32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.4,37,37.8,39)
F=map(fahrenheit,temp)
C=map(celsius,F)

print(F)
print(C)

alist = map(lambda x:x+1,[1,2,3,4,5])
print(alist)

alist = map(lambda x,y,z:x+y+z,[1,2,3,4,5],[1,1,1,1,1],[1,1,1,1,1])
print(alist)


