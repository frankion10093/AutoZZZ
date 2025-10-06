import os
import sys
import time

import subprocess
import pyautogui as pg
import pydirectinput as pyd

from  tool import Template

def start_game():
    arr = None
    if os.path.exists('zzz.txt'):
        print('路径已经存在,从文件中读取中》》》')
        with open("zzz.txt",'r') as f:
            arr = f.readline()
        f.close()
    else:
        while(1):
            print('未找到入口')
            #弹出提示框，用户输入路径
            arr = pg.prompt(title='获取入口',text = '请将绝区零的.exe文件放入',default = '')
            #判断路径是否存在
            #获取到路径用户可能会多加入引号，这里去掉
            arr = arr.strip('"')
            ##判断路径是否存在
            if os.path.exists(arr):
                print(arr)
                #存储路径地址在文件中
                with open("zzz.txt","w") as f:
                    f.write(arr)
                    f.close()
                print('已保存入口')
                break
            else:
                pg.alert(text = "error:路径不存在,请重新输入")
                print('路径不存在,请重新输入')


    if (pg.confirm(text="是否启动脚本？", title="提示", buttons=["是", "否"]) == "是"):
        subprocess.Popen("\"" + arr + "\"")
        print('游戏已启动')
        # 等待游戏启动
        time.sleep(40)
        # 载入游戏
        zairu()
    else:
        sys.exit()


def zairu():
    #判断游戏开始按钮并点击
    Template('zzz/start.png',10,0.6)

    #当前已进入游戏，按下m进入地图选择
    time.sleep(8)
    if Template('zzz/exit.png',5,0.1,False):
        pyd.press('esc')
    time.sleep(3)