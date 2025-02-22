import random

list = ["戎昕语", "赵紫妍", "陈嘉玲"]

while True:
    tips = int(input('\n'"输入1启动程序，输入任意数字退出程序。请输入:"))
    if tips == 1:
        result = random.choice(list)
        print(result)
    else:
        break