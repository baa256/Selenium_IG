from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
import time

# get chrome web driver and open the insta link 
driver = webdriver.Chrome(r'C:\Users\bobo2\AppData\Local\Programs\Python\Python38\chromedriver.exe')
driver.get('https://www.instagram.com/')


# targeting username and password boxes

username = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name = 'username']")))
password = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "input[name = 'password']")))

# clear the box in case the old login is saved 

username.clear()
password.clear()

username.send_keys('') # enter yourt username log in info
password.send_keys('') # ener your password 

time.sleep(1)

log_in = WebDriverWait(  driver , 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR , "button[type = 'submit']"))).click()


# clicking not now when insta asks
not_now = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Not Now')]"))).click()
# clicking the not now when insa asks to save log in info
time.sleep(1)

not_now2 = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//button[contains(text() , 'Not Now')]"))).click()
time.sleep(1)

# search menu

searchbox = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//input[@placeholder = 'Search' ] ")))
searchbox.clear()
time.sleep(2)

keyword = '#'  # enter a hashtag that you want to search in the search bar 
searchbox.send_keys(keyword)

time.sleep(1)

searchbox.send_keys(Keys.RETURN)

time.sleep(1)
# problem here
searchbox.send_keys(Keys.ENTER)

time.sleep(1)


driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path , keyword[1:] + "pics" )

os.mkdir(path)


counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + ' .jpg')
    wget.download(image, save_as)
    counter += 1
    







                                                    

                                                                           
                                                                           
                                                                           
