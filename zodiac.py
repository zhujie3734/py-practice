#tuple示例代码
zodiac_name = ( u'鼠', u'牛', u'虎')
zodiac_days = ((1, 20), (2, 19), (3, 21))

(month, day) = (2, 15)
zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
zodiac_len = len(list(zodiac_day)) % 12
print (zodiac_name[zodiac_len])