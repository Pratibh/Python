__author__ = 'pratibh'

#
fp =open("test.txt","r+")
demo = fp.read()
print(demo)
fp.close()
fp = open("test.txt","r")
fp.read()
print(fp)
fp.close()

