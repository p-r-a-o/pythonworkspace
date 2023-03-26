import os
from tkinter import *
import platform

root = Tk()
root.title("제목 없음 - MAC 메모장")
root.geometry("640x480") # 가로 * 세로

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="편집")
menu.add_cascade(label="편집", menu=menu_edit)

menu_format = Menu(menu, tearoff=0)
menu_format.add_command(label="서식")
menu.add_cascade(label="서식", menu=menu_format)

menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="보기")
menu.add_cascade(label="보기", menu=menu_view)

menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="도움말")
menu.add_cascade(label="도움말", menu=menu_help)

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()
