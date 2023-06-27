#可变长参数
'''
def howlong(first, *other):
    print(1 + len(other))

howlong(123, 234, 456)


var1 = 123

def func():
    var1 += 1
    print(var1)

func()



list1 = [1, 2, 3]
it = iter(list1)
print (next(it))




def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step



#for i in frange(10, 20, 0.5):
#    print(i)



def add(x,y):
    return x+y

x = add(3,5)


'''
from functools import reduce
reduce(lambda x,y: x+y , [2,3,4],1)

