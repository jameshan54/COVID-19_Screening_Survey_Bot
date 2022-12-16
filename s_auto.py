# can automate this program using 
# 1) Task Scheduler 
# 2) could consider python schedule module or cronjobs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time 

# open the web
driver = webdriver.Chrome() 
url = 'https://studenthealthoc.sa.ucsb.edu'
driver.get(url) 
driver.maximize_window()
action = ActionChains(driver) 

# click the student menu
driver.find_element_by_css_selector('#cmdStudentDualAuthentication').click()

# input id, password, and move to next page
driver.find_element_by_css_selector('#txtUsername').send_keys('changhwan')
driver.find_element_by_css_selector('#txtPassWord').send_keys('') # password kept as blank for privacy
driver.find_element_by_css_selector('#cmdStandardProceed').click()

# click complete survey and continue
time.sleep(2)
driver.find_element_by_css_selector('.btn.btn-sm.btn-primary').click()
driver.find_element_by_css_selector('.btn.btn-lg.btn-success').click()

# click no for all
driver.find_element_by_css_selector('#mainbody > main > form > div:nth-child(60) > fieldset > div > div:nth-child(2) > div').click()
driver.find_element_by_css_selector('#mainbody > main > form > div:nth-child(89) > fieldset > div > div:nth-child(2) > div').click()
driver.find_element_by_css_selector('#mainbody > main > form > div:nth-child(118) > fieldset > div > div:nth-child(2) > div').click()
driver.find_element_by_css_selector('#mainbody > main > form > div:nth-child(147) > fieldset > div > div:nth-child(2) > div').click()
driver.find_element_by_css_selector('#mainbody > main > form > div:nth-child(176) > fieldset > div > div:nth-child(2) > div').click()

# click continue
driver.find_element_by_css_selector('#mainbody > footer > div > div.col-xs-6.ta-right > input').click()
