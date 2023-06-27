import re

def find_item(hero):
    with open('sangou.txt' encoding=gb18030) as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero,data)
        print("主角 %s  出现了 %s次 " %(hero,len(name_num))

    return len(name_num)

name_dict = {}
with open('name.txt') as f:
    for line in f:
        name = line.split('|')
        for n in name:
            name_num = find_item(n)
            name_dict[n] = name_num 

name_sorted = sorted(name_dict.item(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

