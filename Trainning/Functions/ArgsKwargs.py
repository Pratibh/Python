__author__ = 'pratibh'


# def only_one(str):
#     print(str)
#
# def multiple(*str):
#     print(str)
#
# only_one("hello")
# multiple("hello","world")
#
# def kwa(**str):
#     for k,v in str.iteritems():
#         print k
#         print v
#
# kwa(name="ram",address="dhapasi")


def test(**names):
    for key,value in names.items():
        print(key)
        print(value)
    print names

def test1(*name):
    print(name)

test1("ram","shyam","hari")
test(name="munmun",age="19",school="dwit")