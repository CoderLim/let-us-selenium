# coding=utf-8

# 需要安装python
#
# 安装pip: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#          python get-pip.py
#
# 下载对应chrome版本的chromedriver: 
#        https://blog.csdn.net/huilan_same/article/details/51896672
#        http://chromedriver.storage.googleapis.com/index.html
# 如果报错: call function result missing 'value'就是因为chrome和chromedriver版本不匹配

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
