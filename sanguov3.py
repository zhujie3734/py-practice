import re

def find_item(hero):
    with open('sangou.txt' encoding=gb18030) as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero,data)
        print("主角 %s  出现了 %s次 " %(hero,len(name_num))

    return len(name_num)

name_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num 

weapon_dict = {}
with open('weapon.txt', encoding='utf-8') as f:
    i = 1
    for line in f:
        if i %2 == 1:
        data = line.strip()
            weapon_num = find_item(data)
            weapon_dict[n] = weapon_num
        i = i + 1


name_sorted = sorted(name_dict.item(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

