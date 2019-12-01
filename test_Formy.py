import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture()
def driver():
    desired_caps = DesiredCapabilities.CHROME
    grid_url = "http://web-jenkins.southeastasia.cloudapp.azure.com:4444/wd/hub"
    driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
    #driver = webdriver.Chrome(chrome_options = options)
    yield driver
    driver.quit()
    # create a object for the chrome driver and pass around

def test_formy_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    assert "Formy" in driver.title
    elem = driver.find_element_by_css_selector('.btn-primary')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-success')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-info')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-warning')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-danger')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector('.btn-link')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Left"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Middle"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="Right"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="1"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//button[text()="2"]')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id('btnGroupDrop1')
    elem.click()
    time.sleep(1)
    
