import tkinter.ttk as ttk
from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("PRAO GUI")
root.geometry("640x480")  # 가로 * 세로



values = [str(i) + "일" for i in range(1,32)] # 1 부터 31 까지의 숫자
combobox = ttk.Combobox(root, height=5,values= values, state="readonly") # 읽기 전용
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 및 버튼 클릭을 통한 값 설정 가능



def btncmd():
    print(combobox.get())


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
