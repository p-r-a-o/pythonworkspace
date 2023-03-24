from tkinter import *

root = Tk()
root.title("PRAO GUI")
root.geometry("640x480")  # 가로 * 세로

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

# pack은 쌓는 느낌, grid는 좌표에 넣는 느낌
# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")

# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)

# 1st line
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 2nd line
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 3rd line
btn_seven = Button(root, text="7", width=5, height=2)
btn_eight = Button(root, text="8", width=5, height=2)
btn_nine = Button(root, text="9", width=5, height=2)
btn_minus = Button(root, text="-", width=5, height=2)

btn_seven.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eight.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_nine.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_minus.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4th line
btn_four = Button(root, text="4", width=5, height=2)
btn_five = Button(root, text="5", width=5, height=2)
btn_six = Button(root, text="6", width=5, height=2)
btn_plus = Button(root, text="+", width=5, height=2)

btn_four.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_five.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_six.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 5th line
btn_one = Button(root, text="1", width=5, height=2)
btn_two = Button(root, text="2", width=5, height=2)
btn_three = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)  # 세로로 합쳐짐

btn_one.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_two.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_three.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)  # 현재 위치로부터 아래쪽으로 더함

# 6th line
btn_zero = Button(root, text="0", width=5, height=2)  # 가로로 합쳐짐
btn_dot = Button(root, text=".", width=5, height=2)

btn_zero.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)  # 현재 위치로부터 오른쪽으로 더함
btn_dot.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()
