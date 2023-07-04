from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
import time

s = Service("D:/GoogleDrive/project/chromedriver.exe")
lvls = []

weapon = str(input('輸入搜尋道具:'))
item = str(input('輸入搜尋詞綴:'))
arrs = list(map(str, input('輸入篩選項目:').split()))

for arr in arrs:
    if arr.startswith("無"):
        arr = "無 " + arr[1:]
        lvls.append(arr)
    elif arr == "":
        pass
    else:
        lvls.append(arr)

# print("裝備:"+weapon)
# print("詞缀:"+item)
# print("屬性:",lvls)

options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get("https://poedb.tw/tw/Modifiers")
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)

WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "py-1"))
)

weapon = driver.find_element(By.LINK_TEXT, weapon)
action = ActionChains(driver).click(weapon).perform()

if lvls:
    for lvl in lvls:
        titles = driver.find_elements(By.CLASS_NAME, "inline-block")
        for title in titles:
            if title.text == lvl:
                action3 = ActionChains(driver).click(title).perform()
                break

time.sleep(1.0)
mods = driver.find_elements(By.CLASS_NAME, 'identify-title')
totals = driver.find_elements(By.CLASS_NAME, 'mod-total')
shot = driver.find_elements(By.CLASS_NAME, 'col-lg-6')
i=0
for mod in mods:
    if mod.text == item:

        action = ActionChains(driver)
        action.move_to_element(totals[i]).perform()
        time.sleep(1)
        
        position = driver.execute_script("""
            var rect = arguments[0].getBoundingClientRect();
            return {left: rect.left, top: rect.top};
            """, shot[i])

        size = shot[i].size
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))

        left,top = position['left'],position['top']
        right = left + size['width']
        bottom = top + size['height']

        im = im.crop((left, top, right, bottom))
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        im.save(f'D:/GoogleDrive/project/POE/screenshot/{current_time}.png')
    i=i+1

driver.quit()