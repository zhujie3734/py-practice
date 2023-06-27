#import os


#print(os.path.abspath('..'))

#print(os.path.exists('/Users'))
#print(os.path.isdir('/Users'))

from pathlib import Path
p = Path('..')
y= [x for x in p.iterdir() if p.is_dir()]
print(y)

q = Path('/tmp/a')
Path.mkdir(q,parents=True)   #上级目录不存在也创建