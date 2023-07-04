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

s = Service("D:/GoogleDrive/project/chromedriver.exe")  #宣告瀏覽器位置
options = Options()
#關閉顯示"Chrom正在受到軟體控制"警語
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

lvls = []   #宣告屬性列表

def mod(item, weapon, arrs):    #宣告mod function，並接收詞綴(item)武器(weapon)屬性(arrs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()    #視窗最大化
    driver.get("https://poedb.tw/tw/Modifiers")     #預設POE詞綴網址
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)    #待網頁開啟後，將畫面移到最頂部

    #避免程式執行太快，加入等待抓到CLASS "py-1"
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "py-1"))
    )

    weapon = driver.find_element(By.LINK_TEXT, weapon)  #抓取網頁中與"武器"字串相同的按鈕
    action = ActionChains(driver).click(weapon).perform()   #使用ActionChains自動點擊(模擬使用者點選)


    if arrs:  #如果有設定"屬性"
        for arr in arrs:
            if arr.startswith("無"):    #如果是無開頭
                arr = "無 " + arr[1:]   #在"無"跟"後面字串"中加入空格
                lvls.append(arr)        #放入lvls列表中
            elif arr == "":             #單存空白就無視
                pass
            else:
                lvls.append(arr)        #剩餘的也放入lvls列表中

        time.sleep(0.5)    #等待0.5s

        titles = driver.find_elements(By.CLASS_NAME, "inline-block")    #抓取CLASS "inline-block"
        #如果使用者的屬性=抓取到CLASS的屬性
        #使用ActionChains自動點擊(模擬使用者點選)
        for lvl in lvls:
            for title in titles:
                if title.text == lvl:
                    action = ActionChains(driver).click(title).perform()
                    break

    if item:    #如果有設定詞綴
        #判別是否是"前綴"/"後綴"
        #不是的話就將字串重新分割，以符合網頁排版
        if len(item) >= 3:
            item = item[:-2] + " " + item[-2:]  #XXX前綴 > XXX 前綴

        time.sleep(0.5)    #等待0.5s
        mods = driver.find_elements(By.CLASS_NAME, 'identify-title')    #抓取詞綴名稱
        totals = driver.find_elements(By.CLASS_NAME, 'mod-total')       #抓取各詞綴結尾位置
        shot = driver.find_elements(By.CLASS_NAME, 'col-lg-6')          #抓取各詞綴位置
        i=0
        for mod in mods:
            if mod.text == item:    #判斷網頁中詞綴是否等於使用者所輸入的
                
                #移動到該詞綴結尾
                action = ActionChains(driver)
                action.move_to_element(totals[i]).perform()
                time.sleep(0.5) #等待0.5s
                
                #抓取該詞綴在螢幕的位置(x,y)
                position = driver.execute_script("""
                    var rect = arguments[0].getBoundingClientRect();
                    return {left: rect.left, top: rect.top};
                    """, shot[i])

                size = shot[i].size #取得該詞綴長寬
                png = driver.get_screenshot_as_png()   #擷取整個畫面
                im = Image.open(BytesIO(png))   #將圖片存入記憶體暫存

                left,top = position['left'],position['top']     #宣告並設定基準位置
                right = left + size['width']                    #宣告並設定右側位置
                bottom = top + size['height']                   #宣告並設定底部位置

                im = im.crop((left, top, right, bottom))    #依據設定的位置裁減截圖
                current_time = time.strftime("%H%M%S", time.localtime())    #抓取即時時間
                im.save(f'D:/GoogleDrive/project/Discord/screenshot/{current_time}.png')    #儲存裁切後的圖片，並用時間當檔名
                url = driver.current_url    #抓取網頁網址

                driver.quit()   #關閉瀏覽器
                return(current_time, url)   #回傳時間(current_time)網址(url)

            i=i+1
    else:   #如果沒有設定詞綴，直接回傳網址
        url = driver.current_url    #抓取網頁網址

        driver.quit()   #關閉瀏覽器
        return(url) #回傳網址(url)