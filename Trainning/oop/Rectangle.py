__author__ = 'pratibh'

class Rectangle:
    def set_length(self,length):
        self.length = length
    def set_breadth(self,breadth):
        self.breadth = breadth
    def get_length(self):
        return self.length
    def get_breadth(self):
        return self.breadth
    def calculate_area(self):
        return self.length*self.breadth

rect1 = Rectangle() #Object for rectangle class
rect1.set_length(10)
rect1.set_breadth(20)
print "Area = ", rect1.calculate_area()
