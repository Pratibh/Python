__author__ = 'pratibh'
from sys import exit
import ast


class Person(object):
    def __init__(self):
        self.name = ""
        self.price = ""
        self.quantity = ""
        self.type = ""
        self.dictionary = {}

    def writing(self):
        self.dictionary[p.name] = p.price, p.quantity, p.type
        target = open('dictionary_information.txt', 'a')
        target.write(str(self.dictionary))
        print self.dictionary

    # Reads from dictionary. Not from the file
    def reading(self):
        name = raw_input("> ")
        if name in self.dictionary:
            print self.dictionary[name]


p = Person()

while True:
    print "Type:\n\t*read to read data base\n\t*write to write to data base\n\t*exit to exit"
    action = raw_input("\n> ")
    if "write" in action:
        p.name = raw_input("Name\n> ")
        p.price = raw_input("Price\n> ")
        p.quantity = raw_input("Quantity\n> ")
        p.type = raw_input("Item Type\n>")
        p.writing()
    elif "read" in action:
        p.reading()
    elif "exit" in action:
        exit(0)
