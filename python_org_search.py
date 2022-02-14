import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += r"F:/Start-With-Selenium"
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_id("id-search-field")
elem.clear()
elem.send_keys("pycons")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
