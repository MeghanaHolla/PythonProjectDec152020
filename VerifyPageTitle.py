from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Training\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
actualTitle = driver.title
if(actualTitle == "Facebook – log in or sign up"):
    print("Test Case Passed")
else:
    print("Test Case Failed")

driver.close()



