from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Training\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.implicitly_wait(30)

#Making changes to Script after R1.1
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("INDEX").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Actions").click()
