# 1-10 event number power result

alist = []
for i in range(1,11):
    if (i%2 == 0):
        alist.append(i*i)
print(alist)

blist = [i*i for i in range(1,11) if (i%2 == 0)]
print(blist)
