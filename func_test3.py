def line(a,b):
    def add(x):
        return a*x + b
    return add

line1 = line(3,5)

print(line1(10))
