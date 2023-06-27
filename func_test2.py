def count():
    cnt = 0
    def addone():
        cnt += 1
        return cnt
    return addone

num1 = count()
print(num1())
#print(num1())

cnt = [0]
type(cnt)