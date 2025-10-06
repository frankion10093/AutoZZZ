import sys
import time

import pyautogui as pg
import pydirectinput as pyd

#图像识别模版
# src: 图像路径
# max_try: 最大尝试次数
# confidence: 置信度阈值
# bool: 是否点击
# stop_time: 完成点击停止时间 ：秒  过场动画时间一般为2秒

### 这个模版函数为通用的图像识别函数
def Template(src:str,max_try:int,confidence:float,bool:bool=True,stop_time:int=1):
    while True:
        try:
            location = pg.locateOnScreen(src, confidence)
            print(f'找到按钮，位置: {location}')
            if bool:
                pg.click(location)
                time.sleep(2)
            return location
        except Exception as e:
            time.sleep(stop_time)
            print(f'图像识别错误: {e}')
            max_try-=1
        if max_try == 0:
            if  bool:
                pg.alert('查到到最大尝试次数，请检查游戏是否已启动')
                sys.exit(1)
            else:
                print('判断失效，软处理')
                return False


#str: 按下具体哪个按钮
#tm: 持续时间 秒
def move(dist:str,tm:float):
    pyd.keyDown(dist)
    time.sleep(tm)
    pyd.keyUp(dist)