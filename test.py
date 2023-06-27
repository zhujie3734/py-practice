import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
#print(p.match('2018-5-10').group(1))
print(p.search('aaa2018-5-10').group(1))
#year, month, day = p.match('2018-5-10').groups()
#print(year, month, day)