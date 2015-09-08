__author__ = 'pratibh'
from sys import exit
import ast


class Person(object):
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.age = ""
        self.whip = {}

    def writing(self):
        self.whip[p.name] = p.age, p.address, p.phone
        target = open('deed.txt', 'a')
        target.write(str(self.whip))
        print self.whip

    def reading(self):
        with open('deed.txt', 'r') as f:
            s = f.read()
            self.whip = ast.literal_eval(s)


p = Person()

while True:
    print "Type:\n\t*read to read data base\n\t*write to write to data base\n\t*exit to exit"
    action = raw_input("\n> ")
    if "write" in action:
        p.name = raw_input("Name?\n> ")
        p.phone = raw_input("Phone Number?\n> ")
        p.age = raw_input("Age?\n> ")
        p.address = raw_input("Address?\n>")
        p.writing()
    elif "read" in action:
        p.reading()
    elif "exit" in action:
        exit(0)
