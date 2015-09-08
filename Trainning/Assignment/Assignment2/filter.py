__author__ = 'pratibh'

def func(d) :
    x=d.keys()
    print "The passed students are:"
    for k in x :
        if(d[k]>=40) :
            print k

di ={"sagar":90,"pratibh":32,"arun":89,"shankar":91,"ramesh":39,"Hari":40}
func(di)