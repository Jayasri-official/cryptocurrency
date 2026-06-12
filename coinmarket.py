from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://coinmarketcap.com")

time.sleep(5)