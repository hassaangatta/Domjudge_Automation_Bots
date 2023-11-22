from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import openpyxl 
 
path = "Excel file"
 
wb_obj = openpyxl.load_workbook(path) 

sheet_obj = wb_obj.active 

uname = []
passw = []

for col in range (1,3):
	for row in range (1,92):
		cell_obj = sheet_obj.cell(row, col)
		if col == 1:
			uname.append(cell_obj.value)
		else:
			passw.append(cell_obj.value)

print(uname)
print(passw)


driver = webdriver.Chrome()

SERVER_ADDR = 'Server ip'
ADMIN_PASS = 'admin password'

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
for i in range (1,92):
	driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[1]/div[2]/ul/li[7]/a').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/p/a[1]').click()
	username = driver.find_element(By.ID, 'team_icpcid')
	username.send_keys(450+i)
	username = driver.find_element(By.ID, 'team_name')
	username.send_keys(uname[i-1])
	username = driver.find_element(By.ID, 'team_displayName')
	username.send_keys(uname[i-1])
	drpcat = Select(driver.find_element(By.ID, 'team_category'))
	drpcat.select_by_value('9')
	drpus = Select(driver.find_element(By.ID, 'team_addUserForTeam'))
	drpus.select_by_value("dont-add-user")
	driver.find_element(By.ID, 'team_save').click()
	driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/table/tbody/tr[7]/td/a').click()
	username = driver.find_element(By.ID, 'user_username')
	username.send_keys(uname[i-1])
	username = driver.find_element(By.ID, 'user_name')
	username.send_keys(uname[i-1])
	username = driver.find_element(By.ID, 'user_plainPassword')
	username.send_keys(passw[i-1])
	check = driver.find_element(By.ID, 'user_user_roles_3')
	check.click()
	sleep(4)
	driver.find_element(By.XPATH, '//*[@id="user_save"]').click()
	driver.find_element(By.XPATH, '/html/body/nav/a').click()

driver.quit()
