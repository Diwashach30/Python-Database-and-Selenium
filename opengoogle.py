import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://www.google.com/")
book_name = "python"
search = browser.find_element(by="name", value="q")
search.send_keys(book_name)

search.submit()
time.sleep(60)
browser.quit()



