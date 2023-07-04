from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

s = Service("D:/GitHub/project/chromedriver.exe")

item = str(input('輸入搜尋項目:'))
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
