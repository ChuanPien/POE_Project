from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
with open('setting.json', 'r', encoding='utf8')as J:
    j = json.load(J)

s = Service(j['driver'])

def start(item):
    driver = webdriver.Chrome(service=s)
    driver.get("https://poedb.tw/tw/garden")

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "select2-option_id2-container"))
    )

    box = driver.find_element(By.ID, "select2-option_id2-container")
    action = ActionChains(driver).click(box).perform()

    search = driver.find_element(By.CLASS_NAME, "select2-search__field")
    search.send_keys(item)
    search.send_keys(Keys.RETURN)

    send = driver.find_element(By.CLASS_NAME, "ml-1")
    action2 = ActionChains(driver).click(send).perform()

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "longstory"))
    )

# items = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/table/tbody")
# items = driver.find_elements(By.CLASS_NAME, "longstory")
# for item in items:
    # print(item.text)

# driver.quit()
