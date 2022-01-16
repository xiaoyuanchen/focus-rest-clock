import os
import sys
import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pygame


focus_and_rest_time = []
quiet_or_music = []
music_path = []
music_mode = []
music_id = 0


def sysout():
    sys.exit(0)


def gui_err1():
    gui = tk.Tk()
    gui.protocol('WM_DELETE_WINDOW', my_close)
    width = 300
    height = 100
    screenwidth = gui.winfo_screenwidth()
    screenheight = gui.winfo_screenheight()
    gui.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    gui.title("提示！")  # 窗口标题
    group = tk.LabelFrame(gui, text="", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    tk.Label(group, text="错误：空路径，请至少存放一首音乐至该路径下！").grid(row=2, column=0, sticky=tk.W)
    def next():
        gui.destroy()
        gui3()
    tk.Button(group, text="返回", font=("", 10), command=next).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(group, text="退出", font=("", 10), command=sysout).grid(row=3, column=1, sticky=tk.E)
    tk.mainloop()


def gui_err2():
    gui = tk.Tk()
    gui.protocol('WM_DELETE_WINDOW', my_close)
    width = 300
    height = 100
    screenwidth = gui.winfo_screenwidth()
    screenheight = gui.winfo_screenheight()
    gui.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    gui.title("提示！")  # 窗口标题
    group = tk.LabelFrame(gui, text="", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    tk.Label(group, text="错误：请输入正确路径！").grid(row=2, column=0, sticky=tk.W)
    def next():
        gui.destroy()
        gui3()
    tk.Button(group, text="返回", font=("", 10), command=next).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(group, text="退出", font=("", 10), command=sysout).grid(row=3, column=1, sticky=tk.E)
    tk.mainloop()



def musics(music_p, musicmode):
    if os.path.isdir(music_p):
        files = []
        if len(os.listdir(music_p)) > 0:
            for file in os.listdir(music_p):
                file_path = os.path.join(music_p, file)
                files.append(file_path)
            if musicmode == 1: # 随机
                random.shuffle(files)
            return files
        else:
            gui_err1()
    else:
        gui_err2()


def my_close(): # 关闭窗口事件
    # True or Flase
    res = messagebox.askokcancel('提示', '是否关闭窗口')
    if res == True:
        sysout()


# 第一个界面
def gui1():
    global focus_and_rest_time
    focus_and_rest_time = []
    gui = tk.Tk()
    gui.protocol('WM_DELETE_WINDOW', my_close)
    width = 310
    height = 150
    screenwidth = gui.winfo_screenwidth()
    screenheight = gui.winfo_screenheight()
    gui.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    gui.title("alarm-clock-pro") #窗口标题
    group = tk.LabelFrame(gui, text="请设置专注时间和休息时间", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    tk.Label(group, text="专注时间/整数分钟：").grid(row=1, sticky=tk.W)
    tk.Label(group, text="休息时间/整数分钟：").grid(row=2, sticky=tk.W)
    v1 = tk.IntVar() # 定义整数变量
    v1.set(45)  # 设定默认值
    v2 = tk.IntVar()
    v2.set(10)
    tk.Entry(group, textvariable=v1).grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)
    tk.Entry(group, textvariable=v2).grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
    def next():
        global focus_and_rest_time
        focus_and_rest_time.append(v1.get())
        focus_and_rest_time.append(v2.get())
        gui.destroy()
        gui2()
    tk.Button(group, text="下一步", font=("", 10), command=next).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(group, text="退出", font=("", 10), command=sysout).grid(row=3, column=1, sticky=tk.E)
    tk.mainloop()

# 第二个界面
def gui2():
    global quiet_or_music
    quiet_or_music = []
    gui = tk.Tk()
    gui.protocol('WM_DELETE_WINDOW', my_close)
    width = 300
    height = 130
    screenwidth = gui.winfo_screenwidth()
    screenheight = gui.winfo_screenheight()
    gui.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    gui.title("alarm-clock-pro")  # 窗口标题
    group = tk.LabelFrame(gui, text="------- 休息时候，要来点音乐放松下吗 ？ ----------", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    v = tk.IntVar()
    v.set(1)
    tk.Radiobutton(group, text="那就放松下     ", variable=v, value=1).grid(row=1, column=0, sticky=tk.W)
    tk.Radiobutton(group, text="不了，让我静静", variable=v, value=0).grid(row=1, column=1, sticky=tk.W)
    tk.Label(group, text="").grid(row=2, column=0, sticky=tk.W)
    def next():
        global quiet_or_music
        quiet_or_music.append(v.get())
        gui.destroy()
        gui3()
    tk.Button(group, text="下一步", font=("", 10), command=next).grid(row=3, column=0, sticky=tk.W)
    tk.Button(group, text="返回", font=("", 10), command=gui1).grid(row=3, column=1, sticky=tk.E)
    tk.mainloop()

# 第三个界面
def gui3():
    global music_path
    music_path = []
    gui = tk.Tk()
    gui.protocol('WM_DELETE_WINDOW', my_close)
    width = 300
    height = 150
    screenwidth = gui.winfo_screenwidth()
    screenheight = gui.winfo_screenheight()
    gui.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    gui.title("alarm-clock-pro")  # 窗口标题
    group = tk.LabelFrame(gui, text="请指定存放音乐的文件夹", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    tk.Label(group, text="文件夹路径：").grid(row=1, sticky=tk.W)
    v1 = tk.StringVar()
    tk.Entry(group, textvariable=v1).grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)
    v2 = tk.IntVar()
    v2.set(1)
    tk.Radiobutton(group, text="随机", variable=v2, value=1).grid(row=2, column=0, padx=5, pady=5)
    tk.Radiobutton(group, text="顺序", variable=v2, value=0).grid(row=2, column=1, padx=5, pady=5)
    def next():
        global music_path
        music_path.append(v1.get())
        music_mode.append(v2.get())
        gui.destroy()
        clock()
    tk.Button(group, text="下一步", font=("", 10), command=next).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(group, text="返回", font=("", 10), command=gui2).grid(row=3, column=1, padx=5, pady=5)
    tk.mainloop()


# 闹钟功能
def clock():
    global music_id
    # 加载用户设置
    music_p = music_path[0] #音乐路径
    study_time = focus_and_rest_time[0] #专注时间
    rest_time = focus_and_rest_time[1] #休息时间
    quietormusic = quiet_or_music[0] #是否要音乐
    musicmode = music_mode[0] #随机或循环

    # print(music_p, musicmode)
    # print(quietormusic)

    # 获取音乐文件列表
    musics_list = musics(music_p, musicmode)
    # print(musics_list)
    le = len(musics_list)
    global start_focus
    start_focus = datetime.now() #缓存开始专注时点
    while True: # ”专注-休息“模式循环
        # 专注界面：显示当前时间
        gui_focus = tk.Tk()
        gui_focus.protocol('WM_DELETE_WINDOW', my_close)
        width = 500
        height = 60
        screenwidth = gui_focus.winfo_screenwidth()
        screenheight = gui_focus.winfo_screenheight()
        gui_focus.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        gui_focus.title("凡诸艺业，未有学而不得者，病在心力懈怠，不能专精耳")  # 窗口标题
        txt = "专注中：  " + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        focus_label = tk.Label(gui_focus, text=txt)
        focus_label.pack()
        tk.Button(gui_focus, text="退出", font=("", 10), command=sysout).pack()
        def focus_beat():
            if (datetime.now() - start_focus).seconds <= (study_time * 60):
                txt = "专注中：  " + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
                focus_label.config(text=txt)
                gui_focus.update()
                focus_label.after(1000, focus_beat)
            else:
                gui_focus.destroy()
        focus_label.after(1000, focus_beat)
        gui_focus.mainloop()

        # 休息界面：显示当前时间，并启动音乐（如果quietormusic为1）
        start_rest = datetime.now()  # 缓存开始休息时点
        if quietormusic == 1: # 初始化并播放音乐
            # print('音乐')
            pygame.mixer.init()  # 初始化
            pygame.mixer.music.load(musics_list[music_id])  # 加载音乐
            pygame.mixer.music.play()  # 播放音乐

        gui_rest = tk.Tk()
        gui_rest.protocol('WM_DELETE_WINDOW', my_close)
        width = 500
        height = 60
        screenwidth = gui_rest.winfo_screenwidth()
        screenheight = gui_rest.winfo_screenheight()
        gui_rest.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        gui_rest.title("一张一弛谓之文武之道")
        txt = "休息中：  " + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        rest_label = tk.Label(gui_rest, text=txt)
        rest_label.pack()
        tk.Button(gui_rest, text="退出", font=("", 10), command=sysout).pack()
        def rest_beat():
            global music_id
            global start_focus
            if ((datetime.now() - start_rest).seconds <= (rest_time * 60)): # 休息未结束
                txt = "休息中：  " + datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
                rest_label.config(text=txt)
                gui_rest.update()
                if quietormusic == 1:
                    if not pygame.mixer.music.get_busy():  # 音乐停
                        music_id += 1
                        if music_id == le:  # 循环音乐列表
                            music_id = 0
                        pygame.mixer.music.load(musics_list[music_id])  # 加载下一首音乐
                        pygame.mixer.music.play()
                rest_label.after(1000, rest_beat) # 1秒后重复执行自己
            else: # 休息结束
                if quietormusic == 1:
                    pygame.mixer.music.stop()
                gui_rest.destroy()
                start_focus = datetime.now() # 重新开始专注
        rest_label.after(1000, rest_beat)
        gui_rest.mainloop()


if __name__ == "__main__":
    gui1()
