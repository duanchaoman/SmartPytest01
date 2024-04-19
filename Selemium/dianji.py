from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import time
def wait_for_element_01(brow, by, value):
    return WebDriverWait(brow,'60').until(
        EC.presence_of_element_located((by, value))
    )

def send_keys(element, text):
    element.send_keys(text)

def click_element(element):
    element.click()

def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

brow = webdriver.Chrome()
brow.maximize_window()
url = brow.get('http://192.168.1.253/SmartSecurity/')

user = wait_for_element_01(brow, By.CLASS_NAME, 'input1')
send_keys(user, '5229102')

pwd = wait_for_element_01(brow, By.CLASS_NAME, 'input2')
send_keys(pwd, 'Admin@123')

login = wait_for_element_01(brow, By.CLASS_NAME, 'lblbtn')
click_element(login)

malarmre = wait_for_element_01(brow, By.CLASS_NAME, 'p-e-a')
click_element(malarmre)

setalarmtime = wait_for_element_01(brow, By.XPATH, '/html/body/div/section/div/section[2]/section/main/div[2]/div/div[1]/div/form/div[1]/div/div/input')  #选择报警时间
click_element(setalarmtime)

settime = wait_for_element_01(brow, By.CLASS_NAME, 'is-plain')
click_element(settime)

setaddress = wait_for_element_01(brow, By.XPATH, '/html/body/div/section/div/section[2]/section/main/div[2]/div/div[1]/div/form/div[2]/div/div/div[1]/div[1]/input')  #设置报警地点
click_element(setaddress)

setbuild = wait_for_element_01(brow, By.XPATH, '//li[3]/label/span/span') #选择模型
click_element(setbuild)

setpoint = wait_for_element_01(brow, By.XPATH, '/html/body/div/section/div/section[2]/section/main/div[2]/div/div[1]/div/form/div[2]/div/div/div[2]/i') #选择建筑点
click_element(setpoint)

time.sleep(10)

move_and_click(999, 424)  # 点击屏幕指定坐标

setevent = wait_for_element_01(brow,By.CLASS_NAME, 'xh-highlight')
click_element(setevent)

setalarmevent = wait_for_element_01(brow,By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[3]')   #选择事件
click_element(setalarmevent)

setalarmpre = wait_for_element_01(brow,By.XPATH,'/html/body/div[1]/section/div/section[2]/section/main/div[2]/div/div[1]/div/form/div[5]/div/div[1]/input')  #设置报警人
send_keys(setalarmpre, '罗冰寒')

setalarmtxt = wait_for_element_01(brow, By.CLASS_NAME, 'el-textarea_inner')  #设置报警描述
send_keys(setalarmtxt, '这是由自动化测试生成的一则人工警情')

setalarmsubmit = wait_for_element_01(brow, By.CLASS_NAME, 'm-l20')  #提交
click_element(setalarmsubmit)