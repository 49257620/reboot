# encoding: utf-8
# Author: LW

import os
import shutil
import time

path = 'C:\\Users\\HP\\Desktop'
target_path = 'E:\\文档\\temp'
time_step = 60 * 60 * 24 * 60

file_names = os.listdir(path)
print('桌面文件共计：', len(file_names))
files = [['DIR' if os.path.isdir(path + os.sep + f) else 'FILE', path + os.sep + f, f,
          time.gmtime(os.stat(path + os.sep + f).st_mtime)] for f in file_names if
         os.stat(path + os.sep + f).st_mtime > time.time() - time_step and not f.endswith('.lnk')]
print('需清理文件共计：', len(files))
for f in files:
    try:
        if not os.path.exists(target_path + os.sep + time.strftime("%Y", f[3])):
            os.mkdir(target_path + os.sep + time.strftime("%Y", f[3]))
        if not os.path.exists(target_path + os.sep + time.strftime("%Y", f[3]) + os.sep + time.strftime("%Y-%m-%d",
                                                                                                        f[3])):
            os.mkdir(target_path + os.sep + time.strftime("%Y", f[3]) + os.sep + time.strftime("%Y-%m-%d", f[3]))
        shutil.move(f[1], target_path + os.sep + time.strftime("%Y", f[3]) + os.sep + time.strftime("%Y-%m-%d",
                                                                                                    f[3]) + os.sep)
        print('成功：', f[2], time.strftime("%Y-%m-%d", f[3]))
    except Exception as e:
        print('失败：', e, f[2], time.strftime("%Y-%m-%d", f[3]))

        # print(time.strftime("%Y-%m-%d %H:%M:%S", f[2]))

if not os.path.exists(target_path + os.sep + '2018'):
    os.mkdir(target_path + os.sep + '2018')

"""


print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))
print(time.ctime(time.time()))
t_second =  time.time()
t_tuple = time.gmtime(t_second)
print(t_tuple)
t_second = t_second - 60*60*24*30
t_tuple = time.gmtime(t_second)
print(t_tuple)
"""
# files = [ 'DIR' if os.path.isdir(path+os.sep+f) else 'FILE',f,time.ctime(os.stat(path+os.sep+f).st_mtime) for f in file_list ]
# for f in file_list:
#    full_path = path+os.sep+f
#    print('DIR' if os.path.isdir(full_path) else 'FILE',f,time.ctime(os.stat(full_path).st_mtime))

# shutil.copyfile(path+os.sep+'Edit.010',path+os.sep+'Edit.015')
