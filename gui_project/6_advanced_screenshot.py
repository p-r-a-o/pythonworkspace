import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 2023년 3월 26일 21시 37분 30초 -> _20230326_213730
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(cur_time))


keyboard.add_hotkey("F1", screenshot)  # 사용자가 F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc")  # 사용자가 esc를 누를 때까지 프로그램 수행
