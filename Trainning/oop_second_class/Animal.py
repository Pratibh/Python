__author__ = 'pratibh'


class Animal:
    # def __init__(self):
    #     print("Default Constructor")
    def __init__(self,name):
        self.name_in_constructor = name
    def setName(self,name):
        self.name_in_class = name



# dog = Animal()
dog1 = Animal("Doggy1")
# dog.setName("Doggy")
# print dog1.name_in_class
print dog1.name_in_constructor