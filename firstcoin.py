from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://coinmarketcap.com")

time.sleep(5)

coin = driver.find_element(By.XPATH, "(//p[contains(@class,'coin-item-name')])[1]")

print("First Coin:", coin.text)

driver.quit()