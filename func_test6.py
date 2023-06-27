fd = open(name.txt)
try:
    for line in fd:
        print(line)
finally:
    fd.close

with open(name.txt) as f:   #上下文管理器，异常后会自动关闭
    for line in f:
        print(line)
    