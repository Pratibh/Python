__author__ = 'pratibh'

import time

ticks = time.time()
print(ticks)

localtime = time.localtime(ticks)
print localtime

print time.asctime(localtime)

print "current date ",time.strftime("%Y:%m:%d",localtime)
print time.strftime("%H//%M//%S",localtime)