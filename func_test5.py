from multiprocessing.resource_sharer import stop


def new_tips (argv):
    def tips(func):
        def nei(a,b):
            print('start %s %s' %(argv, func.__name__))
            func(a,b)
            print('stop')
        return nei
    return tips

@new_tips('add')
def add(a,b):
    print(a+b)

print(add(4,5))