__author__ = 'pratibh'


class Access:
    def __init__(self, a, b, c):
        self.a = a  # public
        self._b = b  # protected
        self.__c = c  # private

    def printPrivate(self):
        return self.__c


acc = Access(1, 2, 3)
print acc.a
print acc._b
# print acc.__c
print acc.printPrivate()
