import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

s = Service("D:/project/chromedriver.exe")
weapen = ""
atts = []

item = str(input('輸入搜尋道具(可空白):'))
mod = list(map(str, input('輸入詞綴(0~6):').split()))
x = len(mod)

if x > 6:
    print('超過可輸入個數\n請從新輸入')

driver = webdriver.Chrome(service=s)
driver.get("https://poedb.tw/tw/xyz")

if item:
    seritem = driver.find_element(By.ID, "autosearch")
    seritem.send_keys(item)
    time.sleep(1)
    btns = driver.find_elements(By.CLASS_NAME, "ui-menu-item-wrapper")
    weapen = btns[0].text
    action = ActionChains(driver).click(btns[0]).perform()
else:
    weapen = "無搜尋道具"


if x >= 1:
    for i in range(x):
        box = driver.find_element(By.ID, f"select2-mods{i}-container")
        action = ActionChains(driver).click(box).perform()
        ser = driver.find_element(By.CLASS_NAME, "select2-search__field")
        ser.send_keys(mod[i])
        ser.send_keys(Keys.RETURN)
        if box.get_attribute('title'):
            atts.append(box.get_attribute('title'))
        else:
            atts.append("無相關詞綴")
else:
    atts.append("無搜尋詞綴")

    

btn = driver.find_element(By.CLASS_NAME, "btn-success")
action = ActionChains(driver).click(btn).perform()

try:
    amount = driver.find_element(By.XPATH, "/html/body/div[1]/div/h4")
    q = [int(temp)for temp in amount.text.split() if temp.isdigit()]
except:
    q = 0
    
Link = driver.current_url

print(Link)
print(q)
print(weapen)
print(atts)

driver.quit()
