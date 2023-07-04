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
import time, json
with open('setting.json', 'r', encoding='utf8')as J:
    j = json.load(J)

s = Service(j['driver'])
options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

lvls = []

def mod(item, weapon, arrs):
    if arrs:
        for arr in arrs:
            if arr.startswith("無"):
                arr = "無 " + arr[1:]
                lvls.append(arr)
            elif arr == "":
                pass
            else:
                lvls.append(arr)


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
        time.sleep(1)
        for lvl in lvls:
            titles = driver.find_elements(By.CLASS_NAME, "inline-block")
            for title in titles:
                if title.text == lvl:
                    action = ActionChains(driver).click(title).perform()
                    break

    if item:
        if len(item) >= 3:
            item = item[:-2] + " " + item[-2:]

        time.sleep(1)
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
                im.save(f'D:/GoogleDrive/project/Discord/screenshot/{current_time}.png')
                url = driver.current_url

                driver.quit()
                return(current_time, url)

            i=i+1
    else:
        url = driver.current_url

        driver.quit()
        return(url)