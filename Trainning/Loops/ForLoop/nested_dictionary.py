__author__ = 'pratibh'

dict={1:{1:'something',2:'nothing'}}

for key,value in dict.items():
    print(key)
    print(value)
    print("******")
    for k,v in value.items():
        print(k)
        print(v)