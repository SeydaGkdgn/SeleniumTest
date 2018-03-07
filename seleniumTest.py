from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path = '/Users/mircom/Desktop/geckodriver')
browser.get("https://www.amazon.com/") #task step1
time.sleep(6)
#----------------------------------------------------------------------
#task step2
giris_yap = browser.find_element_by_css_selector('#nav-link-accountList > span:nth-child(1)')
giris_yap.click()

email = browser.find_element_by_id("ap_email")
email.send_keys("seydagokdogan96@gmail.com")

time.sleep(3)
loginGo = browser.find_element_by_id("continue")
loginGo.click()

password = browser.find_element_by_id("ap_password")
password.send_keys("295069ktu")

signIn = browser.find_element_by_id("signInSubmit")
signIn.click()
#-----------------------------------------------------------------
#task step3

searchText = browser.find_element_by_id("twotabsearchtextbox")
searchText.send_keys("Samsung")
searchButton = browser.find_element_by_class_name("nav-input")
searchButton.click()
#-----------------------------------------------------------------
#task step4

#--------------------------------------------------------
#task step5.1
nextPage = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[5]/div/div/span[3]/a')
nextPage.click()

time.sleep(3)

#task step5.2


#-----------------------------------------------------------------------------
#task step6
thirdProduct = browser.find_element_by_css_selector('#result_18 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h2:nth-child(1)')
thirdProduct.click()

addToList = browser.find_element_by_id('add-to-wishlist-button-submit')
addToList.click()
time.sleep(2)
createWish = browser.find_element_by_xpath('/html/body/div[4]/input')
createWish.click()
#----------------------------------------------------------
#task step7
time.sleep(2)
viewList = browser.find_element_by_css_selector('#WLHUC_viewlist > span:nth-child(1) > span:nth-child(1)')
viewList.click()
#------------------------------------------------------------------
#task step8


#-----------------------------------------------------------------------
#task step-9
time.sleep(1)

delete = browser.find_element_by_class_name("submit.deleteItem")
delete.click()
#-------------------------------------------------------------------
#task step-10

#---------------------
#firefox closed :
#browser.quit()
