import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:\automation\browser_driven\chromedriver.exe")
# chrome驱动安装目录

def openPage(url, myTime, errorRate):
    global driver
    # 打开网址
    driver.get(url)
    # 随机选择一片文章
    randomButtom = driver.find_element_by_id('suiji_a')
    randomButtom.click()
    # 打字时间
    wastTime = driver.find_element_by_id('time')
    wastTime.clear()
    wastTime.send_keys(myTime)
    # 点击打字按钮
    clickTest = driver.find_element_by_name('start_button')
    clickTest.click()
    # 进入打字页面
    for x in range(0, 30):
        divId = 'i_' + str(x)
        # 选中对应序号的一组元素
        dataString = driver.find_element_by_id(divId)
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
