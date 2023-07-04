import time, json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
with open('setting.json', 'r', encoding='utf8')as J:
    j = json.load(J)

s = Service(j['driver'])
atts = []

def shop(item, mod):
    x = len(mod)

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
        weapen = ""

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

    btn = driver.find_element(By.CLASS_NAME, "btn-success")
    action = ActionChains(driver).click(btn).perform()

    try:
        amount = driver.find_element(By.XPATH, "/html/body/div[1]/div/h4")
        q = [int(temp)for temp in amount.text.split() if temp.isdigit()]
    except:
        q = 0

    Link = driver.current_url
    driver.quit()

    return(Link,weapen,atts,q)

    
