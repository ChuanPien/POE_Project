from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json
with open('setting.json', 'r', encoding='utf8')as J:
    j = json.load(J)

s = Service(j['driver'])

def start():
    a = 0

    driver = webdriver.Chrome(service=s)
    driver.get("https://www.dcard.tw/f")

    items = driver.find_elements(By.CLASS_NAME, "kfHo")
    arr = [[0 for i in range(2)] for j in range(len(items))]
    for item in items:
        arr[a][0] = item.text
        arr[a][1] = item.get_attribute('href')
        a += 1

    driver.quit()
    return arr

# print(start())