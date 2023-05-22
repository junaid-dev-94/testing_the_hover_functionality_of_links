import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# create a path variable using chrome services and replace the chrome driver path with the directory wher you have paste your chromedriver.exe file 
PATH = Service('C:\Program Files (x86)\chromedriver.exe')
op = webdriver.ChromeOptions()
# set the driver variable
driver = webdriver.Chrome(service=PATH, options=op)

# create a instance of ActionChains Class
actions = ActionChains(driver)

# Replace the website url with your own url
driver.get("https://www.python.org/")

# this code will wait for the element to be appeared on the page 
driver.implicitly_wait(5)

# you can replace the id with your specified id 
top_bar = driver.find_element(By.ID, 'top')

# this code will fetch all the HTML element with the tag name li in the topbar
top_bar_item = top_bar.find_elements(By.TAG_NAME, 'li')

# this loop will execute the each item once unless you put a condition here
for item in top_bar_item:
    # code to hover over elemets 
    actions.move_to_element(item).perform()
    time.sleep(2)
# this will quit the driver operations  
driver.quit()
   