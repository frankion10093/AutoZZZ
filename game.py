import sys
import time

import pyautogui as pg
import pydirectinput as pyd

from tool import Template,move


def game():
    renwu_1()
    if  get_jiangli_1():
        get_jiangli_2()
        return
    renwu_2()
    if get_jiangli_1():
        get_jiangli_2()
        return
    renwu_3()
    get_jiangli_1()
    get_jiangli_2()








#任务1：完成每日咖啡
def renwu_1():
    pyd.press('m')
    time.sleep(2)
    #进入地图快捷导航
    Template('zzz/map.png', 10, 0.5)
    #点击第一张图
    Template('zzz/map_1.png', 10, 0.5)

    #选择列表咖啡店
    Template('zzz/kafei.png', 10, 0.5)

    #确认进入
    Template('zzz/que_ren.png', 10, 0.5)
    time.sleep(2)
    #往前走对话触发,完成每日咖啡
    time.sleep(2)
    move('w',3)
    pyd.press('f')
    # time.sleep(1)
    if  not Template('zzz/heikafei.png', 4, 0.5,False):
        x,y=pg.size()
        pg.click(x/2, y/2)
        time.sleep(1)
        return
    Template('zzz/heikafei.png', 10, 0.5)
    Template('zzz/kafei_queren.png', 10, 0.5)
#任务2：完成占卜
def renwu_2():
    #点开菜单a
    pyd.press('f2')
    laocation = Template('zzz/renwu_2.png', 10, 0.5, False)
    pg.click(laocation.left+laocation.width/2,laocation.top+laocation.height/1.1)
    time.sleep(1)

    #跳转到占卜页面
    Template('zzz/que_ren.png', 10, 0.5,stop_time=5)

    pyd.press('f')
    time.sleep(2)
    if Template('zzz/yikai.png', 8, 0.5,False):
        pyd.press('esc')
        time.sleep(2)
        return
    Template('zzz/kai.png', 10, 0.5)
    x,y=pg.size()
    pg.moveTo(x/2, y/2)
    pyd.mouseDown()
    for i in range(6):
        pg.moveTo(x/2+300,y/2+300,duration=1)
        pg.moveTo(x/2,y /2,duration=1)
    pyd.mouseUp()
    time.sleep(6)
    Template('zzz/zhanbu_queren.png', 10, 0.5)
    Template('zzz/jieqian_queren.png', 10, 0.5)
    pyd.press('esc')
    time.sleep(2)
#任务3：完成录像店经营
def renwu_3():
    #点开菜单a
    pyd.press('f2')
    laocation = Template('zzz/renwu_3.png', 10, 0.5, False)
    pg.click(laocation.left+laocation.width/2,laocation.top+laocation.height/1.1)
    # time.sleep(1)
    #跳转到录像店经营界面
    Template('zzz/que_ren.png', 10, 0.5,stop_time=5)
    pyd.press('f')
    time.sleep(2)
    Template('zzz/chakan.png', 10, 0.5)
    # time.sleep(1)
    if  Template('zzz/zhengzai.png', 8, 0.5,False):
        pyd.press('esc')
        time.sleep(2)
        return
    Template('zzz/quxiao.png', 10, 0.5)

    Template('zzz/tianjia.png', 10, 0.5)

    Template('zzz/queding.png', 10, 0.5)

    Template('zzz/luxiang.png', 10, 0.5)

    Template('zzz/tuijian.png', 10, 0.5)

    Template('zzz/yingye.png', 10, 0.5)

    Template('zzz/yingye_queren.png', 10, 0.5)

    Template('zzz/yingye_queren.png', 10, 0.5)

    pyd.press('esc')
    time.sleep(3)
#任务4：完成日奖励领取
def get_jiangli_1():
    pyd.press('f2')
    time.sleep(2)
    if  Template('zzz/mantili.png', 5, 0.4,False):
        if Template('zzz/jiangli.png', 5, 0.5,False):
            Template('zzz/jiangli.png', 10, 0.5)
            Template('zzz/lingqu_queren.png', 10, 0.5)
            pyd.press('esc')
            time.sleep(2)
        else:
            print('日常已经完成并且领取')
        pyd.press('esc')
        return True
    else:
        print('日常未完成')
        pyd.press('esc')
        return False

#任务5：完成月奖励领取
def get_jiangli_2():
    time.sleep(2)
    pyd.press('f3')
    Template('zzz/chengzhangrenwu.png',10,0.1)

    if  Template('zzz/quanbulingqu.png', 5, 0.4,False):
        Template('zzz/quanbulingqu.png', 10, 0.4)

    Template('zzz/dengjihuikui.png', 10, 0.1)

    if Template('zzz/zhoujiangli.png', 5, 0.6, False):
        Template('zzz/zhoujiangli.png', 10, 0.6)

    pyd.press('esc')
    time.sleep(2)
    pg.hotkey('alt','f4')
    print('全部完成,退出游戏')





