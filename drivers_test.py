import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#------------------------------
permitNumber ='S000000000000'
BDay = 'MMDDYY'
today = date.today()
url = "https://drive.mn.gov"
horule = '===================='
#------------------------------

print(horule)
print("< debug >")
print(today)
print(url)
print("Permit: " + permitNumber)
print("DOB: " + BDay)
print(horule)

browser = webdriver.Firefox()
browser.maximize_window()
browser.get(url)

print("Opened Browser. Now going through click steps")
print(horule)

time.sleep(1)
browser.find_element(By.LINK_TEXT, 'Schedule an Appointment').click()
time.sleep(1)
browser.find_element(By.XPATH, "//span[contains(text(), 'Driver Services')]").click()
time.sleep(1.5)
browser.find_element(By.XPATH, "//span[contains(text(), 'Class D Skill Exam - Retest')]").click()

print("Filling in Applicant Information")
print(horule)

time.sleep(1)
browser.find_element(By.ID, 'Dk-e').send_keys(permitNumber + Keys.TAB)
time.sleep(1)
browser.find_element(By.ID, 'Dk-h').send_keys(BDay + Keys.RETURN)
browser.find_element(By.XPATH, "//span[contains(text(), 'Next')]").click()

print("Finished Filling out information")
print(horule)

time.sleep(1)
browser.find_element(By.XPATH, "//button[contains(text(), 'OK')]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//span[contains(@class, 'FIC FICSmall CaptionIcon FICF FICF_Material FICFTAuto')]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//span[contains(text(), 'With Available Appointments')]").click()
time.sleep(1)
browser.find_element(By.XPATH, "//span[contains(@class, 'FIC FICSmall CaptionIcon FICF FICF_Material FICFTAuto')]").click()

print("Finished \ntoDo: email available appointments \nCtrl + C to quit \nOr close browser window")
print(horule)
