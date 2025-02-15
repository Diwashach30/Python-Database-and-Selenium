import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://www.daraz.com.np/#?")
valentine_gift = "teddy bear"
search = browser.find_element(by="name", value="q")
search.send_keys(valentine_gift)



search.submit()
time.sleep(60)
browser.quit()



