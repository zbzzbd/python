from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

browser = webdriver.Firefox()
try:
    browser.get("http://sso.ggang.cn/SSoOperater/SSoLoginIndex?url=http://www.ggang.cn/")
    browser.find_element_by_name("loginName").send_keys("13611873856")
    browser.find_element_by_xpath("//input[@type='password']").send_keys("123456")
    browser.find_element_by_id("btnLogin").click()
    browser.get_cookies()
    # browser.get("http://www.ggang.cn/News/Newsitem/105470")
    # browser.implicitly_wait(5)
    # video = browser.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/div[3]/span/embed")
    # url=browser.execute_script("return arguments[0].currentSrc;",video)
    #
    # print url
except NoSuchElementException as e:
    print e
finally:
    print (ctime())
    browser.get_screenshot_as_file("E:\\screentPage\\vide.jpg")
    browser.implicitly_wait(10)
    browser.quit()
