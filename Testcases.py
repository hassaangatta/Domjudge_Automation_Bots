from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
driver = webdriver.Chrome()

# MODIFY THESE VALUES !!!!!!!!!
PROBLEM_DIR = 'Directory path/'
PROBLEM_ID = 'XX'
SERVER_ADDR = 'http://172.16.xx.xx:XXXX/public'
ADMIN_PASS = 'Ts2VIFkU8LXFQD-a'
driver.get(SERVER_ADDR)
driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
username = driver.find_element(By.ID, 'username')
username.send_keys('admin')
password = driver.find_element(By.ID, 'inputPassword')
password.send_keys(ADMIN_PASS)
driver.find_element(By.XPATH, '//*[text()="Sign in"]').click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/logout"]'))
)
driver.find_element(By.CSS_SELECTOR, 'a[href="/jury/problems"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/jury/problems/' + PROBLEM_ID + '"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/jury/problems/' + PROBLEM_ID + '/testcases"]').click()

inputs = []
outputs = []
for input in os.listdir(PROBLEM_DIR + '/in'):
    inputs.append(os.path.join(os.getcwd(), PROBLEM_DIR + '/in/' + input))

for output in os.listdir(PROBLEM_DIR + '/out'):
    outputs.append(os.path.join(os.getcwd(), PROBLEM_DIR + '/out/' + output))
    
for i in range(0, len(inputs)):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add_input"))
    )
    driver.find_element(By.ID, "add_input").send_keys(inputs[i])
    driver.find_element(By.ID, "add_output").send_keys(outputs[i])
    driver.find_element(By.XPATH, '/html/body/div/div/div/form/input').click()

sleep(1)
driver.quit()
