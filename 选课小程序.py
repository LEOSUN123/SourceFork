from selenium.webdriver.support.ui import WebDriverWait
import os
import pyautogui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tesserocr

# #更改工作目录
# check=os.path.isdir(os.getcwd()+'/自动选课')
# if not check:
#     os.mkdir(os.getcwd()+'/自动选课')
# os.chdir(os.getcwd()+'/自动选课')

#获取屏幕尺寸
width=str(int((pyautogui.size()[0])/1.25))
height=str(int((pyautogui.size()[1])/1.25))
size='--window-size='+width+'x'+height

def rob():
    # 目标网站
    site = 'https://i.sjtu.edu.cn/xtgl/login_slogin.html'
    # 用户名
    user = entry11.get()
    # 密码
    password = entry21.get()
    # 课程名称
    coursename = entry31.get()
    #验证码的位置
    ul=int(entry51.get())
    ur=int(entry52.get())
    dl=int(entry53.get())
    dr=int(entry54.get())
    #课程的性质
    category=entry41.get()
    #选课按钮的位置
    takebutton=entry61.get()


    from selenium import webdriver
    co = webdriver.ChromeOptions()
    co.add_argument('--headless')
    co.add_argument('--no-sandbox')
    co.add_argument('--disable-dev-shm-usage')
    co.add_argument(size)
    print('程序开始运行')
    browser = webdriver.Chrome(chrome_options=co)

#进入登录界面
    def login(browser, site):
        browser.get(site)
        wait = WebDriverWait(browser, 10)
        Jaccount = wait.until(EC.element_to_be_clickable((By.ID, 'jAccount')))
        Jaccount.click()
        content = browser.title
        return browser
#登录账号
    counter = 1
    print("尝试登录")
    content = "上海交通大学统一身份认证"
    while content == "上海交通大学统一身份认证":

        if counter > 3:
            from tkinter import messagebox
            messagebox.showinfo("糟糕", "登录失败")
            print("登录失败")
            exit(1)
            break

        browser=login(browser,site)
        wait = WebDriverWait(browser, 10)
        input1 = wait.until(EC.presence_of_element_located((By.ID, 'input-login-user')))
        input1.clear()
        input1.send_keys(user)
        input2 = browser.find_element(By.ID, 'input-login-pass')
        input2.clear()
        input2.send_keys(password)
        input3 = browser.find_element(By.ID, 'input-login-captcha')

        browser.save_screenshot('print_screen.png')
        from PIL import Image
        i = Image.open("print_screen.png")  # 打开上面保存的全屏截图图片

        # # 无头模式下运行
        # rangle_headless = (ul, ur, dl, dr)
        # frame4 = i.crop(rangle_headless)
        # frame4.save('verify_code.png')

        # 有头模式下的代码
        rangle = (1360, 434, 1500, 480)
        frame4 = i.crop(rangle)
        frame4.save('verify_code.png')  # 保存为验证码的截图图片



        image = Image.open('verify_code.png')
        yanzhengma = tesserocr.image_to_text(image)
        print("第" + str(counter) + "次验证码：" + yanzhengma)
        input3.clear()
        input3.send_keys(yanzhengma)
        content = browser.title
        counter = counter + 1

    print("---------------------")

    # 记录一下当前handle(为了跳转回该页面做铺垫)
    currentHandle = browser.current_window_handle
    xuanke = browser.find_elements(By.ID, 'drop1')[2]
    xuanke.click()
    target = browser.find_element(By.CSS_SELECTOR, '#cdNav > ul > li.dropdown.open > ul > li:nth-child(3) > a')
    target.click()

    # 跳转到新的想要跳转的页面
    for handle in browser.window_handles:
        # 切换到新的页面
        browser.switch_to.window(handle)
        # 可以在新的页面中找到一些特有属性，作为判断依据
        if handle.title == '自主选课':
            break

    # 这时因为已经跳转到想要跳转的页面了，所以此时的标题就是新页面的标题了
    print(browser.title)

    def begin():

        wait = WebDriverWait(browser, 10)
        if category=='通识课':
            # 点击，通识课模块
            xuanxiuke = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tab_kklx_10')))
            xuanxiuke.click()
        elif category=='主修课程':
            #点击主修课程模块
            xuanxiuke = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tab_kklx_01')))
            xuanxiuke.click()
        elif category=='公共选修课':
            #点击公选模块
            xuanxiuke = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tab_kklx_11')))
            xuanxiuke.click()

        # 搜索框内输入课程名称
        search = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#searchBox > div > div.row.search-filter > div > div > div > div > input')))
        search.clear()
        search.send_keys(coursename)
        # 点击搜索
        consult = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#searchBox > div > div.row.search-filter > div > div > div > div > span > button.btn.btn-primary.btn-sm')))
        consult.click()
        # 点击选课按钮
        takeit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, takebutton)))
        takeit.click()

        browser.refresh()

    from tkinter import messagebox
    messagebox.showinfo("恭喜", "运行成功！请安心等待，在选课成功前，不要关闭程序")
    root.destroy()
    print("开始抢课……")
    error = 0
    while error < 20:
        try:
            begin()
        except:
            error += 1
            print('请检查选课情况')



from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('自动选课系统')
root.geometry('550x500')
def Instructions():
    import os
    os.startfile(os.getcwd()+'/help.docx')
label11 = Label(root, text="您的JAccount账号名：")
label11.grid(row=0, column=0, padx=10, pady=10)
entry11 = Entry(root, width=20)
entry11.grid(row=0, column=1,columnspan=4, padx=10, pady=10)
entry11.insert(0, 'leo.sun')

label21 = Label(root, text="您的JAccount密码：")
label21.grid(row=1, column=0, padx=10, pady=10)
entry21 = Entry(root, width=20)
entry21.grid(row=1, column=1,columnspan=4, padx=10, pady=10)
entry21.insert(0, '78694265264@Sxk')

label31 = Label(root, text="您要抢选的课程全名：")
label31.grid(row=2, column=0, padx=10, pady=10)
entry31 = Entry(root, width=20)
entry31.grid(row=2, column=1,columnspan=4,padx=10, pady=10)
entry31.insert(0, '固定收益证券分析')

label41 = Label(root, text="该课程的性质(主修课程/通识课/公共选修课)：")
label41.grid(row=3, column=0, padx=10, pady=10, sticky=W)
entry41 = Entry(root, width=20)
entry41.grid(row=3, column=1,columnspan=4,padx=10, pady=10)
entry41.insert(0, '主修课程')

label51 = Label(root, text="您的验证码位置（请阅读说明书后更改）：")
label51.grid(row=4, column=0, pady=10)

entry51 = Entry(root, width=5)
entry51.grid(row=4, column=1)
entry51.insert(0, '1085')
entry52 = Entry(root, width=5)
entry52.grid(row=4, column=2)
entry52.insert(0, '347')
entry53 = Entry(root, width=5)
entry53.grid(row=4, column=3)
entry53.insert(0, '1203')
entry54 = Entry(root, width=5)
entry54.grid(row=4, column=4)
entry54.insert(0, '383')

label61 = Label(root, text="选课按钮的CSS路径")
label61.grid(row=5, column=0, pady=10)

entry61 = Entry(root, width=20)
entry61.grid(row=5, column=1,columnspan=4)
entry61.insert(0, '#btn-xk-184271FDE4A7363EE065F8163EE1DCCC')

b3 = Button(root, text='开始抢课', command=rob)
b3.grid(row=6, column=0, columnspan=6,padx=10, pady=5)
b4 = Button(root, text='阅读说明书', command=Instructions)
b4.grid(row=7, column=0, columnspan=6,padx=10, pady=5)
label71 = Label(root, text="*以上默认数据为示例数据，您需要选择对其进行更改；")
label71.grid(row=8, column=0, columnspan=6, padx=10, pady=5, sticky=W + E)
label81 = Label(root, text="请勿将该程序用于非法用途，如有任何问题开发者不负责任")
label81.grid(row=9, column=0, columnspan=6, padx=10, pady=5, sticky=W + E)
label91 = Label(root, text="版权所有@Sxk_melancholy")
label91.grid(row=10, column=0, columnspan=6, padx=10, pady=5, sticky=W + E)

root.mainloop()

# 78694265264@Sxk

