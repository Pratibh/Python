__author__ = 'pratibh'

class Coordinate:
    def __init__(self,x_coordinate,y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __add__(self, other):
        new_coordinate=[]
        x = self.x_coordinate+other.x_coordinate
        y = self.y_coordinate +other.y_coordinate
        new_coordinate.append(x)
        new_coordinate.append(y)
        return new_coordinate

point1 = Coordinate(1,1)
point2 = Coordinate(2,1)
print point1+point2


