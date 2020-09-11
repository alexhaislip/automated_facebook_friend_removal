from selenium.common.exceptions import NoSuchElementException


def friendsornot(driver, time):

    friend_button_path = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[' \
                         '4]/div/div/div/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div/span'

    remove_friend_multiple_options = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[' \
                                     '1]/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div/span'

    remove_friend_single_option = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[' \
                                  '1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/span'\

    current_num_of_friends = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                          '1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div['
                                                          '1]/div/div/div/div[1]/a[3]/div/span/span[2]').text

    print("Your current number of friends: " + current_num_of_friends)

    while check_exists_by_xpath(driver, friend_button_path) == True:

        friend_button = driver.find_element_by_xpath(friend_button_path)
        friend_button.click()

        time.sleep(2)


        if check_exists_by_xpath(driver, remove_friend_multiple_options) == True:
            
            # Click the single option

            multiple = driver.find_element_by_xpath(remove_friend_multiple_options)
            multiple.click()

        elif check_exists_by_xpath(driver, remove_friend_single_option) == True:
            
            # Click menu item from multiple items
            single = driver.find_element_by_xpath(remove_friend_single_option)
            print("Single Located")
            single.click()
            print("Single Clicked")

        else:
            print("neither elements found")

        confirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div['
                                               '1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]')
        confirm.click()

        current_num_of_friends = int(current_num_of_friends) - 1

        print("SUCESSFULL UNFRIEND: " + str(current_num_of_friends))

        driver.refresh()


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
