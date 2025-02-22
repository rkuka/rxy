import tkinter as tk
from tkinter.messagebox import*

def push(target,code,possition):
    try:
        with open(target,"r",encoding="utf-8") as t:
            line = t.readlines()
        line.insert(possition,code+'\n')
        with open(target,"w",encoding="utf-8") as f:
            f.writelines(line)
            showinfo("Tips","程序执行成功")
    except FileNotFoundError as n:
        showwarning("WARNING",f"找不到目标文件,{n}")
    except Exception as e:
        showerror("ERROR",f"错误,{e}")

root = tk.Tk()
root.title("注销程序")

def send():
    try:
        target1 = target1_entry.get()
        push(target=target1,code="'''",possition=0)
    except Exception as x:
        showerror("ERROR",f"错误,{x}")

def _exit_():
    root.destroy()

target1_lable = tk.Label(root,text="文件名:")
target1_lable.pack(pady=6)

target1_entry = tk.Entry(root)
target1_entry.pack(pady=6)

start = tk.Button(root,text="确定",command=send)
start.pack(pady=6)

end = tk.Button(root,text="退出",command=_exit_)
end.pack(pady=6)

root.mainloop()