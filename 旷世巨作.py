import tkinter as tk
from tkinter.messagebox import *
def push(target,code,possition):
    try:
        with open(target,"r",encoding="utf-8") as f:
            line = f.readlines()
        if possition<0 or possition>len(line):
            showerror("WARNING","此位置不可插入")
            return
        line.insert(possition,code+'\n')
        with open(target,"w",encoding="utf-8") as f:
            f.writelines(line)
            showinfo("Tips","代码插入成功")
    except FileNotFoundError as n:
        showerror("WARNING",f"无法找到目标文件,{n}")
    except Exception as e:
        showwarning("WARNING",f"{e}")
root = tk.Tk()
root.title("自动化插入代码")
def send():
    try:
        target1 = target1_entry.get()
        possition1 = int(possition1_entry.get())
        code1 = code1_entry.get()
        push(target1,code1,possition1)
    except Exception as t:
        showerror("WARNING",f"{t}")
def _exit():
    root.destroy()
target1_lable = tk.Label(root,text="程序名:")
target1_lable.pack(pady=5)
target1_entry = tk.Entry(root)
target1_entry.pack(pady=5)
code1_lable = tk.Label(root,text="代码:")
code1_lable.pack(pady=5)
code1_entry = tk.Entry(root)
code1_entry.pack(pady=5)
possition1_lable = tk.Label(root,text="位置:")
possition1_lable.pack(pady=5)
possition1_entry = tk.Entry(root)
possition1_entry.pack(pady=5)
begin = tk.Button(root,text="确定",command=send)
begin.pack(pady=5)
end = tk.Button(root,text="退出",command=_exit)
end.pack(pady=5)
root.mainloop()