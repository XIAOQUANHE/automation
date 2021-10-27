from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver_path = 'D:/automation/browser_driven/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('http://bosssit.shinebed.com.cn/user/login')
sleep(2)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'right').click()
sleep(2)
driver.find_element(By.ID,'username').send_keys('50754')
driver.find_element(By.ID,'password').send_keys('123456')
sleep(2)
driver.find_element(By.XPATH,"//*[@id='formLogin']/div[4]/div/div/span/button").click()
sleep(6)
driver.close()