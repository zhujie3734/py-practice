
def print_params_4(x, y, z=3, *pospar, **keypar):
    print (x,y,z)
    print (pospar)
    print (keypar)

print_params_4(1,2,3,4,5,6,7, foo=1, bar=2)