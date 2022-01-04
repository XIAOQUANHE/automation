import sys
import os.path
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

current_path = os.path.dirname(__file__)    # 获取当前目录
driver_path = Service(os.path.join(current_path,'../browser_driven/chromedriver.exe'))   # 和当前的驱动目录拼接完整
driver = webdriver.Chrome(service=driver_path)      # executable_path即将被弃用，改为service
# chrome驱动安装目录
# sys.exit()      # 程序断点

def openPage(url, myTime, errorRate):
    global driver
    # 打开网址
    driver.get(url)
    sys.exit()      # 程序断点
    # 随机选择一片文章
    randomButtom = driver.find_element(By.ID,'suiji_a')
    randomButtom.click()
    # 打字时间
    wastTime = driver.find_element(By.ID,'time')
    wastTime.clear()
    wastTime.send_keys(myTime)
    # 点击打字按钮
    clickTest = driver.find_element(By.ID,'start_button')
    clickTest.click()
    # 进入打字页面
    for x in range(0, 30):
        divId = 'i_' + str(x)
        # 选中对应序号的一组元素
        dataString = driver.find_element(By.ID,divId)
        # 提取文本
        inputText = dataString.find_element_by_tag_name('span')
        # 使用空格进行文本分词
        contentList = inputText.text.split(" ")
        # 选中输入框
        inputClick = dataString.find_element_by_class_name('typing')
        # 遍历每个单词
        for y in contentList:
            for a in y:
                # print(random.randint(1,100))
                # 出错
                if random.randint(1, 100) <= errorRate:
                    inputClick.send_keys("+")
                    time.sleep(0.1)
                    inputClick.send_keys(Keys.BACK_SPACE)
                    time.sleep(0.1)
                    inputClick.send_keys(a)
                # 正确
                else:
                    inputClick.send_keys(a)
                time.sleep(0.3)
            # 词末空格
            inputClick.send_keys(Keys.SPACE)


def main():
    # 打字网站
    url = "https://dazi.kukuw.com/"
    # 打字时间
    myTime = 3
    # 错误率，百分之五
    errorRate = 5
    openPage(url, myTime, errorRate)


if __name__ == '__main__':
    main()
