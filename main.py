import os
import sys
from decouple import config
from selenium import webdriver
import time


try:
    URL = config("URL")
    URL2 = config("URL2")
    URL3 = config("URL3")
    Username = config("USER")
    Password = config("PASS")
    #obviously change this to wherever your webdriver is located
    driver_path = './driver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless')
    driver = webdriver.Chrome(driver_path, options=options)
    #go to the login site
    driver.get(URL)
    Username_xpath = '//*[@id="input_1"]'
    Username_area = driver.find_element_by_xpath(Username_xpath)
    Username_area.send_keys(Username)
    Password_xpath = '//*[@id="input_2"]'
    Password_area = driver.find_element_by_xpath(Password_xpath)
    Password_area.clear()
    Password_area.send_keys(Password)
    submit_xpath = '/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td/input'
    submit_area = driver.find_element_by_xpath(submit_xpath)
    submit_area.click()
    #wait for the approved screen
    time.sleep(.5)
    driver.get(URL2)
    Username_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/input'
    Username_area = driver.find_element_by_xpath(Username_xpath)
    Username_area.send_keys(Username)
    Password_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/input'
    Password_area = driver.find_element_by_xpath(Password_xpath)
    Password_area.clear()
    Password_area.send_keys(Password)
    submit_xpath = '//*[@id="LO"]'
    submit_area = driver.find_element_by_xpath(submit_xpath)
    submit_area.click()
    #wait for the approved screen
    time.sleep(1)
    submit_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/input'
    submit_area = driver.find_element_by_xpath(submit_xpath)
    submit_area.click()
    driver.get(URL3)
    time.sleep(1)
    table = driver.find_element_by_xpath("/html/body/table/tbody[2]")

    for row in table.find_elements_by_xpath('/html/body/table/tbody[2]'):
        if "P452" in row.text:  # if station in table
            row.click()
            time.sleep(1)
            address = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/small')
            details = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/small')
            stop = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/small')
            print(stop.text)
            with open("list.txt", "w") as f:
                text = f"{address.text}\n\n{details.text}\n\n{stop.text}"
                f.write(text)

except:
    raise os.system("msg * Something went wrong")