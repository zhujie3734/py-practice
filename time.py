#import time

#print(time.time())
#print(time.localtime())
#print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
oneday = datetime.datetime(2018,5,27)
newday = datetime.timedelta(days=10)
print(oneday + newday)