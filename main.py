import argparse
import os
import time
import PySimpleGUI as sg

from selenium import webdriver

from functions import delete_friends


def main():

    layout = [[sg.Text('Simple Window')],
              [sg.InputText()],
              [sg.Submit()],
              [sg.Cancel()]]

    window = sg.Window('Window title', layout)
    event, value = window.read()
    window.close()
    text_input = value[0]
    sg.popup('You enterd', text_input)

    # TODO GUI updates below:
    # need username and password in gui (also friend list config)
    # limit friend adds and deletes, and other stuff
    # run button

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

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

    delete_friends(driver, time)

if __name__ == '__main__':
    main()
