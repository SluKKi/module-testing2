from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://google.com")

print(driver.title)
driver.quit()