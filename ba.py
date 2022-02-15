# 모바일 버젼 크롤링 방법
# from selenium import webdriver
# mobile_emulation = { "deviceName": "iPhone X" }
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Chrome(options=chrome_options)

from selenium import webdriver
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.keys import Keys
from datetime import datetime


warnings.filterwarnings(action='ignore')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("--start-maximized")
options.add_argument("disable-gpu")
options.add_argument('--incognito')



def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

makedirs('result/kor')

today_date = datetime.today().strftime("%m%d")

kws = [ '하나님의교회', '안상홍','하나님의교회', '안상홍']
f_name = ['교회명(데스크탑)_'+today_date+'.png','아버지함자(데스크탑)_'+today_date+'.png','교회명(모바일)_'+today_date+'.png','아버지함자(모바일)_'+today_date+'.png']

print(f_name[0])
print(f_name[1])
print(f_name[2])
print(f_name[3])

num = 0

#검색결과 버튼 클릭
for kw in kws:



    driver = webdriver.Chrome('C:\ptest\chromedriver', options=options)
    driver.get('https://www.youtube.com/')

    wait = WebDriverWait(driver, 10)
    time.sleep(3)

    search = driver.find_element_by_name('search_query')
    search.send_keys(Keys.RETURN)
    search.send_keys(kw)
    search.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    time.sleep(1)

    endkey = 15  # / 늘릴때 마다 20개
    while endkey:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)
        endkey -= 1

    ele = driver.find_element_by_xpath('//*[@id="page-manager"]')
    total_height = ele.size["height"]
    driver.implicitly_wait(1)
    driver.set_window_size(1920, total_height)  # the trick
    driver.implicitly_wait(1)
    driver.save_screenshot(f_name[num])
    driver.implicitly_wait(1)



    print(f_name[num]+ '완료!')
    num = num + 1
    driver.implicitly_wait(1)

driver.close()