#coding=utf-8
import os    
import sys
import shutil
import time
import random

srcdir = r"D:\学习培训\SW\K8S"
targetdir = r"D:\学习培训\SW\yaml"
list_dirs = os.walk(srcdir)

time1 = time.localtime()
time_fmt = time.strftime("%Y%m%d%H%M%S",time1)
#def check_dup_filename(filename,checkdir):



for root, dirs, files in list_dirs: 
    for f in files:
        num_prefix = str(random.randint(1,100))
        suffix = os.path.splitext(f)[1]
        if suffix == ".yaml":
            result = os.path.join(root,f)
            #print(result)
            dupfile=os.path.join(targetdir,f)
            #check if target dir contain same name file
            if os.path.exists(dupfile) == False:
                shutil.move(result, targetdir)
            else:
                newfile=os.path.splitext(f)[0] + time_fmt + num_prefix + suffix   
                os.rename(dupfile,os.path.join(targetdir,newfile))
                shutil.move(result, targetdir)
#           # except Exception as e:
#           #     print('%s' %e)