# -*- coding: utf-8 -*-
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import unittest, time, re, os
import timeit


username = "USER NAME"
access_key = "ACCESS KEY"

class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and 
    def setUp(self):
        desired_caps = {
            "build": 'PyunitTest JFFD build', # Change your build name here
            "name": 'Py-unittest-JFFD', # Change your test name here
            "platform": 'Windows 10', # Change your OS version here
            "browserName": 'Chrome', # Change your browser here
            "version": '87.0', # Change your browser version here
            "resolution": '1024x768', # Change your resolution here
            "console": 'true', # Enable or disable console logs
            "network":'true'   # Enable or disable network logs
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://www.jffd.com/#/")

        #Click on COOKIES ACCEPTED
        check_box_one = driver.find_element_by_css_selector("button.affirm:nth-child(4)")
        check_box_one.click()

        # SHOP DROP DOWN
        elementDD = driver.find_element_by_id("shop")
        action = ActionChains(driver) #create action chain object
        action.click_and_hold(on_element = elementDD) #click and hold the item 
        action.perform() #SHOP DROP DOWN ELEMENT

if __name__ == "__main__":
    unittest.main()
