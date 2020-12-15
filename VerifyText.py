from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Training\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.implicitly_wait(30)

el = driver.find_element_by_id("nav-link-accountList")
hover = ActionChains(driver)
hover.move_to_element(el).perform()

driver.find_element_by_link_text("Account").click()

