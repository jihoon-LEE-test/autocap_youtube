# 모바일 버젼 크롤링 방법
    # from selenium import webdriver
    # mobile_emulation = { "deviceName": "iPhone X" }
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Chrome(options=chrome_options)

from selenium import webdriver
import time
import warnings
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.keys import Keys
from datetime import datetime

warnings.filterwarnings(action='ignore')

def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

now = datetime.now()
now_mon_year = '2022년 '+str(now.month) + '월'
now_month = str(now.month) + '월'
now_year = str(now.year)+'년'
today_date = datetime.today().strftime("%Y%m%d")

ko_file_path = 'Z://05_모니터링//02 구글 모니터링//SERP 1페이지 캡처//구글 한국어 SERP//'+now_year+'//' + now_mon_year +'//'+today_date
eng_file_path = 'Z://05_모니터링//02 구글 모니터링//SERP 1페이지 캡처//구글 영어 SERP//'+now_year+'//' + now_mon_year +'//'+today_date

today_date = datetime.today().strftime("%m%d")

kws = [ '하나님의교회', '안상홍','하나님의교회', '안상홍']
f_name = ['교회명(데스크탑)_'+today_date+'.png','아버지함자(데스크탑)_'+today_date+'.png','교회명(모바일)_'+today_date+'.png','아버지함자(모바일)_'+today_date+'.png']



num = 0


#검색결과 버튼 클릭
for kw in kws:

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('--incognito')

    # 일반데스크탑의 경우
    if num<2:
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome('C:\ptest\chromedriver', options=options)
        driver.get('https://www.youtube.com/')

        wait = WebDriverWait(driver, 10)

        time.sleep(1)
        search = driver.find_element_by_name('search_query')
        search.send_keys(Keys.RETURN)
        search.send_keys(kw)
        search.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        time.sleep(1)

    # 모바일의 경우
    else:
        mobile_emulation = {"deviceName": "iPad Pro"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome('C:\ptest\chromedriver', options=options)
        if num==2:
            driver.get('https://m.youtube.com/results?sp=mAEA&search_query=%ED%95%98%EB%82%98%EB%8B%98%EC%9D%98%EA%B5%90%ED%9A%8C')
        elif num==3:
            driver.get('https://m.youtube.com/results?sp=mAEA&search_query=%EC%95%88%EC%83%81%ED%99%8D')

        wait = WebDriverWait(driver, 10)
        time.sleep(1)



    endkey = 1 # / 늘릴때 마다 20개
    while endkey:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(1)
        endkey -= 1
    #이부분 ele 구하는 값이 잘못됨
    if num<2:
        ele = driver.find_element_by_xpath('//*[@id="page-manager"]')
    else:
        # ele = driver.find_element_by_xpath('//*[@id="page-manager"]')

    total_height = ele.size["height"]
    driver.implicitly_wait(1)
    print(1)
    driver.set_window_size(1920, total_height)  # the trick
    print(1)
    driver.implicitly_wait(1)
    driver.save_screenshot('test.png')
    print(1)
    driver.implicitly_wait(1)



    print(f_name[num]+ '완료!')
    num = num + 1
    driver.implicitly_wait(1)



driver.quit()