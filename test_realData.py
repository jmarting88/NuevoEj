# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import StaleElementReferenceException

class TestRealData():
  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  options.add_argument('headless')
  driver = webdriver.Chrome(options=options)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def page_has_loaded(self):
    print("Checking if {} page is loaded.".format(self.driver.current_url))
    page_state = self.driver.execute_script('return document.readyState;')
    return page_state == 'complete'
  
  def test_realData(self):
    # Test name: Real Data
    # Step # | name | target | value
    # 1 | open | /sso/Login?RL=1&locale=en_US | 
    self.driver.get("https://ndcdyn.interactivebrokers.com/sso/Login?RL=1&locale=en_US")
    # 2 | setWindowSize | 1900x789 | 
    self.driver.set_window_size(1900, 789)
    # 3 | type | id=user_name | jlic2022
    self.driver.find_element(By.ID, "user_name").send_keys("jlic2022")
    # 4 | type | id=password | jlic2021
    self.driver.find_element(By.ID, "password").send_keys("jlic2021")
    # 5 | click | css=.login-page > .container | 
    self.driver.find_element(By.CSS_SELECTOR, ".login-page > .container").click()
    # 6 | click | css=.login-page > .container | 
    self.driver.find_element(By.CSS_SELECTOR, ".login-page > .container").click()
    # 7 | click | id=submitForm | 
    self.driver.find_element(By.ID, "submitForm").click()

    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'bar3-logo__ib')))

    # 8 | open | https://ndcdyn.interactivebrokers.com/AccountManagement/AmAuthentication?action=PORTFOLIOANALYST&tab=HOME | 
    self.driver.get("https://ndcdyn.interactivebrokers.com/AccountManagement/AmAuthentication?action=PORTFOLIOANALYST&tab=HOME")

    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'bar3-logo__ib')))
    """
    try:
      if expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Add/Edit')):    
        # 9 | click | linkText=Add/Edit |
        self.driver.find_element(By.LINK_TEXT, "Add/Edit").click()
        print("click add/")
        # 10 | click | linkText=Reset | 
        self.driver.find_element(By.LINK_TEXT, "Reset").click()
        print("reset")
    except 
    """

    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "filter_pickerText")))
    # 11 | click | name=filter_pickerText | 
    self.driver.find_element(By.NAME, "filter_pickerText").click()
    # 12 | click | name=filter_pickerText | 
    self.driver.find_element(By.NAME, "filter_pickerText").click()
    # 13 | type | name=filter_pickerText | U10347775
    print("set id")
    self.driver.find_element(By.NAME, "filter_pickerText").send_keys("U10347775")
    # 14 | click | css=freeform-text-filter .fa-search | 
    self.driver.find_element(By.CSS_SELECTOR, "freeform-text-filter .fa-search").click()
    # 15 | click | css=picker-entry-icon > .fa-lg |
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, "picker-entry-icon > .fa-lg").click()
    # 16 | click | linkText=Continue | 
    self.driver.find_element(By.LINK_TEXT, "Continue").click()
    # 17 | mouseOver | linkText=Planning |
    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//i[@ng-if="$ctrl.showInfo"]')))
    time.sleep(3)
    elements = self.driver.find_elements(By.XPATH, '//i[@ng-if="$ctrl.showInfo"]')

    intentos = 0
    while intentos <= 3:
      intentos += 1
      try:
        final = elements[1].get_attribute("data-original-title")
        print(final)
        return final
      except StaleElementReferenceException as e:
        elements = self.driver.find_elements(By.XPATH, '//i[@ng-if="$ctrl.showInfo"]')
    
a = TestRealData().test_realData()
