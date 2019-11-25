import sys 
import os 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome('/Users/Nicolas/chromedriver')
browser.get('https://www.facebook.com')


def sg():
    python_button = browser.find_element_by_name("email")  
    python_button.send_keys('nicolas.bourriez@laposte.net')
    python_button = browser.find_element_by_name("pass")
    python_button.send_keys('ardeniboulunialay')
    python_button = browser.find_element_by_id('loginbutton')
    python_button.click()
    python_button = browser.find_element_by_name('q')
    python_button.send_keys('bonjour')

if __name__ == "__main__":
    sg()