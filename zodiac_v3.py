chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = ( u'魔蝎', u'水瓶', u'双鱼', u'白羊', u'金牛', u'双子', u'巨蟹', u'狮子',
                u'处女', u'天平', u'天蝎', u'射手',)
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12,23))

#cz_num = {}
#for i in chinese_zodiac:
#    cz_num[i] = 0
cz_num = {i:0 for i in chinese_zodiac}

z_num= {}
for i in zodiac_name:
    z_num[i] = 0

while True:

    #用户输入
    year = int(input('请输入年份: '))
    month = int(input('请输入月份: '))
    day = int(input('请输入日期: '))

    n = 0 
    while zodiac_days[n] < (month,day):
        if month == 12 and day >= 23:
            break
        n += 1
    print(zodiac_name[n])

    print ('%s 年的生肖是 %s'  % (year, chinese_zodiac[year%12]))

    cz_num[chinese_zodiac[year%12]] += 1
    z_num[zodiac_name[n]] += 1

    #输出统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个'%(each_key,cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个'%(each_key,z_num[each_key]))