# study
# 目标：账号密码登陆，连续输入三次，账号冻结
# 实现：建立账号目录 及 冻结目录，for循环，文本读写
# 依旧存在的问题：
‘’‘1.读写有重复
2.代码掌握不熟悉
3.文件关闭依旧存在问题
主要框架如下：1.大循环三次；2.读入freeze账号list；3.判断账号是否冻结；4.输入账号密码；5.判断账号密码是否为空；6.读入账号密码list；7.比对确认账号密码正确；8.错误写入freeze账号目录；9.关闭文件退出‘’‘
# 代码如下：
#!/usr/bin/env python
# -*- coding:utf-8 -*-
count = 0
name_cook = []
name_list = []
name_freeze_addresss = 'C:/Users/joeya/Desktop/freeze_name.txt'
name_cook_address = 'C:/Users/joeya/Desktop/name_cook_list.txt'
r_name_cook = open(name_cook_address, 'r').read()
name_cook_list = r_name_cook.split()
r_name_freeze = open(name_freeze_addresss, 'r').read()
w_name_freeze = open(name_freeze_addresss,'a')
name_freeze_list = r_name_freeze.split()
for count in range(3):
    count = count + 1
    name = input('please write your name:')
    cook = input('please write your cook:')
    if name in name_freeze_list:
        print('your cookie is freeze!')
        break
    for line in name_cook_list:
        if line is None:
            break
        name_cook.append(line) #name 为单数行，cook 为双数行
    name_number = len(name_cook)
    for i in range(0,name_number,2):
        ture_name = name_cook[i]
        ture_cook = name_cook[i+1]
        if name == ture_name and cook == ture_cook:
            print('right name! welcome!')
            break
    if (3-count)==0:
        print('your cookie is frezee!!!')
        w_name_freeze.write('  %s  ;'%name)
        break
    print('wrong name!please try again!only %d times'%(3-count))
w_name_freeze.close()
