__author__ = 'pratibh'

fp = open("test","w+")
fp.write("arunisagood boy")
print(fp.name)
print(fp.mode)
pos = (fp.tell())
print "the position is",+pos
fp.seek(0)
print "current position ", fp.tell()
# moves cursor to 5th position from first
fp.seek(5,0)
# prints 5 characters
print fp.read(5)
print "current position: ", fp.tell()
print "--------------------"
fp.seek(2,1)
print "current position ",fp.tell()
print fp.read(2)
print "current position ",fp.tell()
fp.close()






