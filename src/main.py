import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def foo():
    driver = webdriver.Chrome()
    driver.get('https://rosa.llsapp.com/my-groups')

    # driver.fullscreen_window()
    search_bar = driver.find_element_by_css_selector("input[placeholder='输入班级名称进行搜索']")
    search_bar.send_keys("7")
    search_bar.send_keys(Keys.RETURN)

    # driver.refresh()
    driver.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
    element = driver.find_element_by_xpath("//*[@id=\"root\"]/section/main/div[1]/div[3]")
    element.click()
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    # print(driver.find_element_by_tag_name('body').text)
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    # print(driver.find_element_by_tag_name('body').text)
    print('done')


if __name__ == "__main__":
    foo()
