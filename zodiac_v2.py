
zodiac_name = ( u'鼠', u'牛', u'虎')
zodiac_days = ((1, 20), (2, 19), (3, 21))


int_month = int(input('请输入月份: '))
int_day = int(input('请输入日期: '))

for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print(zodiac_name[zd_num])
        break

#zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
#zodiac_len = len(list(zodiac_day)) % 12
#print (zodiac_name[zodiac_len])