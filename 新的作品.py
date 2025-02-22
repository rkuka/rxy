import turtle
import tkinter as tk
import time
from tkinter import messagebox
import random


def ___phython___():
    turtle.bgcolor("black")
    turtle.color("white", "red")
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(200)
    turtle.circle(100, 180)
    turtle.right(90)
    turtle.circle(100, 180)
    turtle.forward(200)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    for i in range(len(f"戎昕语姐姐, 网卡被关了哦!")):
        turtle.write(f"戎昕语姐姐, 网卡被关了哦!"[
                     :i+1], align='left', font=('Times New Roman', 30, 'italic'))
        turtle.delay()
        time.sleep(0.1)
    time.sleep(3)
    turtle.done()
    words = "love"
    for item in words.split():
     letterlist = []
     for y in range(20, -20, -1):
      list_X = []
      letters = ''
      for x in range(-30, 30):
       expression = ((x*0.05)**2+(y*0.1)**2-1.5)**3-(x*0.05)**2*(y*0.1)**5
       if expression <= 0:
        letters += item[(x-y) % len(item)]
       else:
        letters += ' '
      list_X.append(letters)
      letterlist += list_X
     print('\n'.join(letterlist))
    root = tk.Tk()
    root.attributes('-fullscree', True)
    root.attributes('-alpha', 0.1)

    def small_window():
        messagebox.showinfo(" ", "戎昕语姐姐, 桌面被控制了哦!")
    button = tk.Button(root, command=small_window, width=root.winfo_screenwidth(
    ), height=root.winfo_screenheight())
    button.pack()
    root.mainloop()


def ___comman___():
    root1 = tk.Tk()
    root1.geometry('100x150+600+300')
    lable = tk.Label(root1, text="大难不死, 必有后福！")
    lable.pack()
    root1.mainloop()


list = [1, 0]
root2 = tk.Tk()
root2.geometry('300x300+600+300')


def ___choice___():
    result = random.choice(list)
    if result == 1:
        ___phython___()
    elif result == 0:
        ___comman___()


button2 = tk.Button(root2, text="开枪", comman=___choice___,
                    width=50, height=100)
button2.pack()
root2.mainloop()
