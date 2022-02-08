import os
import sys
from decouple import config
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    URL = config("URL")
    URL2 = config("URL2")
    URL3 = config("URL3")
    Username = config("USER")
    Password = config("PASS")
    station = "P14"
    #obviously change this to wherever your webdriver is located
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless')
    driver = webdriver.Chrome('./driver.exe', options=options)
    #go to the login site
    driver.get(URL)
    Username_xpath = '//*[@id="input_1"]'
    Username_area = driver.find_element(By.XPATH, Username_xpath)
    Username_area.send_keys(Username)
    Password_xpath = '//*[@id="input_2"]'
    Password_area = driver.find_element(By.XPATH, Password_xpath)
    Password_area.clear()
    Password_area.send_keys(Password)
    submit_xpath = '/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[5]/td/input'
    submit_area = driver.find_element(By.XPATH, submit_xpath)
    submit_area.click()
    #wait for the approved screen
    time.sleep(.5)
    driver.get(URL2)
    Username_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]/input'
    Username_area = driver.find_element(By.XPATH, Username_xpath)
    Username_area.send_keys(Username)
    Password_xpath = '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[3]/td[2]/input'
    Password_area = driver.find_element(By.XPATH, Password_xpath)
    Password_area.clear()
    Password_area.send_keys(Password)
    submit_xpath = '//*[@id="LO"]'
    submit_area = driver.find_element(By.XPATH, submit_xpath)
    submit_area.click()
    #wait for the approved screen
    time.sleep(1)
    submit_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[1]/input'
    submit_area = driver.find_element(By.XPATH, submit_xpath)
    submit_area.click()
    #driver.get(URL3)
    time.sleep(1)
    table = driver.find_element(By.XPATH, "/html/body/table/tbody[1]")
    print("boop")
    for row in table.find_elements(By.XPATH, '/html/body/table/tbody[1]'):
        if station in row.text:  # if station in table

            # Setup wait for later
            wait = WebDriverWait(driver, 10)

            # Store the ID of the original window
            original_window = driver.current_window_handle

            # Check we don't have other windows open already
            assert len(driver.window_handles) == 2

            # Click the link which opens in a new window
            row.click()

            # Wait for the new window or tab
            wait.until(EC.number_of_windows_to_be(3))

            # Loop through until we find a new window handle
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break

            # Wait for the new tab to finish loading content
            wait.until(EC.title_is("IncdSel"))
            time.sleep(1)
            address = driver.find_element(By.XPATH,
                                          '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/small')
            details = driver.find_element(By.XPATH,
                                          '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/small')
            stop = driver.find_element(By.XPATH,
                                       '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/small')
            print(stop.text)
            with open("list.txt", "w") as f:
                text = f"{address.text}\n\n{details.text}\n\n{stop.text}"
                f.write(text)

except:
    raise #os.system("msg * Something went wrong")