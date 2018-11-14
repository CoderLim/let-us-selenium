# coding=utf-8

# 需要安装python、pip
# 下载对应的chromedriver: http://chromedriver.storage.googleapis.com/index.html?path=2.27/

# 导入selenum的webdriver包
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# executable_path设置chromedriver安装的位置（绝对路径）
driver = webdriver.Chrome(chrome_options=option, executable_path='/Users/leeco/Downloads/chromedriver')

# get方法发送网址
driver.get("http://www.baidu.com")

# 通过输入框的id为kw,定位到输入框，输入”selenium”
driver.find_element_by_id('kw').send_keys("selenium")

# 通过搜索按钮的id为su定位到搜索按钮，点击"搜索"
driver.find_element_by_id('su').click()
driver.quit()
