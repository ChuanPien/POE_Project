from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service("D:/GoogleDrive/project/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://poedb.tw/tw/Claws#ModifiersCalc")

mods = driver.find_elements(By.CLASS_NAME, 'col-lg-6')
for mod in mods:
    print(mod.text)

driver.quit()