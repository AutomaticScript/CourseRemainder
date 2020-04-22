import subprocess
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SeleniumTry:
    class_list = [6, 7, 8, 9, 10, 11, 12, 13]
    download_dir = "/home/lida/Desktop/tool/CourseRemainder/input"
    chrome_driver = '/home/lida/Downloads/chromedriver_linux64/chromedriver'
    class_website = 'https://rosa.llsapp.com/my-groups'

    def clicks(self):
        subprocess.run(["rm", "-rf", self.download_dir])
        chrome_options = webdriver.ChromeOptions()
        preferences = {'download.default_directory': self.download_dir}
        chrome_options.add_experimental_option('prefs', preferences)
        driver = webdriver.Chrome(self.chrome_driver,
                                  options=chrome_options)
        driver.get(self.class_website)

        count = 0
        for i in range(len(self.class_list)):
            # search the i-th class tab
            search_bar = WebDriverWait(driver, 30).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='输入班级名称进行搜索']")
                )
            )
            search_bar.clear()
            search_bar.send_keys(self.class_list[i])
            search_bar.send_keys(Keys.RETURN)
            time.sleep(1)
            # fit to click operation
            driver.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
            element = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//*[@id=\"root\"]/section/main/div[1]/div[3]")
                )
            )
            element.click()
            # move to new tab
            count = count + 1
            window_after = driver.window_handles[count]
            driver.switch_to.window(window_after)
            # click to download into ~/Downloads in default
            element = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, "//span[text()='导 出']/..")
                )
            )
            element.click()
            time.sleep(2)
            # move back to the base tab
            window_after = driver.window_handles[0]
            driver.switch_to.window(window_after)

        time.sleep(2)
        driver.quit()
        print('done')


if __name__ == "__main__":
    seleniumTry = SeleniumTry()
    seleniumTry.clicks()
