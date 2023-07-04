from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
      
wb = load_workbook('shop.xlsx')
ws = wb['ID']

s = Service("D:/project/chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://poedb.tw/tw/xyz")

box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/form/div/div[7]/div[1]")
action = ActionChains(driver).click(box).perform()

print('start')
items = driver.find_elements(By.CLASS_NAME, "select2-results__option")
for item in items:
    string = item.get_attribute("id")
    ws.append([string[26:],item.text])
    # print(string[26:],item.text)

print('save')
wb.save('shop.xlsx')
driver.quit()
