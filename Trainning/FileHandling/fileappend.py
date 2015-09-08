__author__ = 'pratibh'

fp = open("test.txt","a")
fp.write("Arun is a good boy")
fp.close()
fp=open("test.txt","r+")
demo = fp.read()
print(demo)
fp.close()
