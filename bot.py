from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

print("test")

time.sleep(5)

driver.get("https://zefoy.com/")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("------------------")
print("jacks tiktok")
print("view bot")
print("------------------")
print(" ")

time.sleep(20)


for n in range(999999):
  try:
    driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
    time.sleep(3)
    bob = driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button")
    bob.click()
    print("Views sent, Sending again in 6 minutes.")
    time.sleep(370)
  except:
    print("Views failed, Trying again in 6 minutes.")
    time.sleep(370)

