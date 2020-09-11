from selenium import webdriver  
import argparse
import os
from functions import friendsornot
import time

def main():

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--headless")

    parser = argparse.ArgumentParser()
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    args = vars(parser.parse_args())
    chromedriver_path = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.implicitly_wait(30)

    base_url = "https://www.facebook.com/haislipalexander/friends"
    driver.get(base_url)
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(args['username'])
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(args['password'])
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    xpath_for_friend = driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                     '1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div['
                                                     '3]/div[1]/div[3]/div/div/div')

    friendsornot(driver,time)

if __name__ == '__main__':
    main()