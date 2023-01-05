from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
def start():
    url = 'https://myship.7-11.com.tw/Home/Main'
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div').click()
    driver.find_element_by_id('login_button').click()          #點擊登入鍵
    
def login(email,password):
    WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="returnUrl"]/button[1]')))
    driver.find_element_by_xpath('//*[@id="returnUrl"]/button[1]').click()     #選擇登入fb
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)          #輸入帳號密碼
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)        
    driver.find_element_by_id('loginbutton').click()

def buy(phone,email):
    url = 'https://myship.7-11.com.tw/general/detail/GM2211081464286'
    driver.get(url)

    while(1):
        try:
            size = WebDriverWait(driver,1,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="divGoodList"]/div/div/div[2]/div[3]/div[1]/div/span[1]')))     #選擇尺寸
            size.click()
            print('已開始')
            break            
        except:
            print('尚未開始拍賣')
            driver.refresh()           

    count = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,'plus')))    #數量+1
    count.click()          

    buynow = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="divGoodList"]/div[1]/div/div[2]/div[3]/div[2]/div[2]/button[2]')))
    buynow.click()             #結帳

    check = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.checkbox>label')))      #勾選同意條款
    check.click()               
    
    driver.find_element_by_xpath('//*[@id="btnNext"]').click()

    ordphone = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="OrdMobile"]')))
    ordphone.send_keys(phone)
    ordemail = WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="OrdEmail"]')))
    ordemail.send_keys(email)
    #driver.find_element_by_xpath('//*[@id="btnNext"]').click()              #送出訂單