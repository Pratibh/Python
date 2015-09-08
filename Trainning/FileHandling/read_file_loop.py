__author__ = 'pratibh'

fp = open("ram_desc.txt","w+r")
fp.write("This is test\n")
fp.write("he is donkey\n")
fp.write("he failed exams\n")
fp.seek(0)
lines = fp.readlines()
print "all lines", lines
for line in lines:
    print(line)