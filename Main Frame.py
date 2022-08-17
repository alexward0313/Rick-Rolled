import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

pyautogui.FAILSAFE = True

def skipad():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("play.png")
        bannerCords = pyautogui.locateCenterOnScreen("bannerad.png")
        blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png")

        if videoAdCords or bannerCords or blackBannerCords is not None:
            break
        
    if videoAdCords is not None:
        pyautogui.click(videoAdCords)
    elif bannerCords is not None:
        pyautogui.click(bannerCords)
    elif blackBannerCords is not None:
        pyautogui.click(blackBannerCords)

    skipad()


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/")

time.sleep(10)

search = driver.find_element("name", "search_query")
search.send_keys("Rick Roll")
search.submit()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Rick Astley - Never Gonna Give You Up (Official Music Video)"))
    )
    element.click()

    skipad()
except:
    driver.quit()

time.sleep(213)

driver.quit()

















