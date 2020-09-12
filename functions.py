from selenium.common.exceptions import NoSuchElementException


def delete_friends(driver, time):

    print("Looking for friends...")

    friend_button_path = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[' \
                         '4]/div/div/div/div/div/div/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div/span'

    remove_friend_multiple_options = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[' \
                                     '1]/div/div/div[1]/div/div[1]/div/div[4]/div[2]/div/div/span'

    remove_friend_single_option = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[' \
                                  '1]/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/span '

    current_num_of_friends = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                          '1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div['
                                                          '1]/div/div/div/div[1]/a[3]/div/span/span[2]').text

    print("Your current number of friends: " + current_num_of_friends)

    while check_exists_by_xpath(driver, friend_button_path):

        friend_button = driver.find_element_by_xpath(friend_button_path)
        friend_button.click()

        print("Clicked friend button...")

        time.sleep(2)

        if check_exists_by_xpath(driver, remove_friend_multiple_options):

            # Click the single option

            multiple = driver.find_element_by_xpath(remove_friend_multiple_options)
            multiple.click()

        elif check_exists_by_xpath(driver, remove_friend_single_option):

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

        print("SUCESSFULLL UNFRIENDED: " + str(current_num_of_friends))

        driver.refresh()


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def add_friends_from_people_you_may_know(driver,time):

    print("Looking for friends...")

    timeline_button_path = '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[' \
                                                       '1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[' \
                                                       '1]/div/div/div/div[1]/a[1]/div'

    adding_friends_button = '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[' \
                            '1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[3]/div[' \
                            '3]/div/div[1]/div[2]/span '

    current_num_of_friends = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                          '1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div['
                                                          '1]/div/div/div/div[1]/a[3]/div/span/span[2]').text

    print("Your current number of friends: " + current_num_of_friends)

    while check_exists_by_xpath(driver, adding_friends_button):

        timeline_button = driver.find_element_by_xpath(timeline_button_path)
        timeline_button.click()

        print("Clicked the timeline button...")

        time.sleep(2)

        if check_exists_by_xpath(driver, remove_friend_multiple_options):

            # Click the single option

            multiple = driver.find_element_by_xpath(remove_friend_multiple_options)
            multiple.click()

        elif check_exists_by_xpath(driver, remove_friend_single_option):

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

        print("SUCESSFULLL UNFRIENDED: " + str(current_num_of_friends))

        driver.refresh()



def remove_active_requests(driver):
    print("test")




