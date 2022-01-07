import sys
import os.path
import time
import random
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from  selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
'''
待优化项：异常处理未完成    2022-1-6
优化项：异常处理已完成      2022-1-7
'''

current_path = os.path.dirname(__file__)    # 获取当前目录
driver_path = Service(os.path.join(current_path,'../browser_driven/chromedriver.exe'))   # 和当前的驱动目录拼接完整
driver = webdriver.Chrome(service=driver_path)      # executable_path即将被弃用，改为service
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
print(picture_time)
# chrome驱动安装目录
# sys.exit()      # 程序断点

def openPage(url, myTime, errorRate):
    global driver
    global picture_time
    # 打开网址
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    # 随机选择一片文章
    randomButtom = driver.find_element(By.ID,'suiji_a')
    randomButtom.click()
    # 打字时间
    wastTime = driver.find_element(By.ID,'time')    # 定位文本框
    wastTime.clear()                                # 如果里面有值就清除掉
    wastTime.send_keys(myTime)                      # 传入自定义的值myTime
    # 点击打字按钮
    clickTest = driver.find_element(By.NAME,'start_button')
    clickTest.click()
    # 进入打字页面
    for x in range(0, 30):
        divId = 'i_' + str(x)
        # 选中对应序号的一组元素
        dataString = driver.find_element(By.ID,divId)   # i_0开始
        # 提取文本
        inputText = dataString.find_element(By.TAG_NAME,'span')     # i_0下的元素定位获取
        # 使用空格进行文本分词
        contentList = inputText.text.split(" ")     # 获取到的数据以text形式输出，并且用空格分割
        # 选中输入框
        inputClick = dataString.find_element(By.CLASS_NAME,'typing')
#------------------------------------------分割线--------------上面代码已经分析完成---------------------------------------------
        # 遍历每个单词
        for y in contentList:
            for a in y:                             # 遍历单词中的字母
                # print(random.randint(1,100))
                # 出错
                if random.randint(1, 100) <= errorRate:
                    '''
                    模拟出错率，随机生成1-100和传入的errorRate进行比较
                    键入错误字符进行退格操作后输入正确字母
                    '''
                    inputClick.send_keys("+")
                    time.sleep(0.1)
                    inputClick.send_keys(Keys.BACK_SPACE)
                    time.sleep(0.1)
                    inputClick.send_keys(a)
                # 正确
                else:
                    try:
                        inputClick.send_keys(a)
                    except ElementNotInteractableException as ET:
                        picture_url = driver.get_screenshot_as_file('D:\\automation\\Picture\\' + picture_time + '.png')
                        print('%s：截图成功！！！' % picture_url)
                        print(ET)
                        driver.quit()
                time.sleep(0.3)
            # 词末空格
            inputClick.send_keys(Keys.SPACE)

def main():
    global picture_time
    # 打字网站
    url = "https://dazi.kukuw.com/"
    # 打字时间
    myTime = 1
    # 错误率，百分之五
    errorRate = 5
    openPage(url, myTime, errorRate)

if __name__ == '__main__':
    main()
