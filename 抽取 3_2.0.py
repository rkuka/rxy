import random

list = ['戎昕语', '赵紫妍', '陈嘉玲']
list2 = ['戎昕语 2', '赵紫妍 2', '陈嘉玲 2']
list3 = ['戎昕语 3', '赵紫妍 3', '陈嘉玲 3']

list4 = [list, list2, list3]

while True:
    for i in random.sample(list4, 1):
        count = 0
    while count < 3:
        tips = int(input('\n'"输入1启动程序，输入任意数字退出程序。请输入:"))
        if tips == 1:
                result = random.choice(i)
                print(result)
                count += 1
    if tips != 1:
        break