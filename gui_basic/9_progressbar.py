import time
import tkinter.ttk as ttk
from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("PRAO GUI")
root.geometry("640x480")  # 가로 * 세로

# # progressbar = ttk.Progressbar(root,maximum=100,mode="indeterminate") # 바가 지나가는 형싱
# progressbar = ttk.Progressbar(root,maximum=100,mode="determinate") # 바가 채워지는 형식
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()
#
#
#
# def btncmd():
#     progressbar.stop() # 작동 중지
#
#
#
# btn = Button(root, text="선택", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트 -> 업데이트를 해줘야 바가 차는 모습을 볼 수 있음
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
