from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service("/Users/konrad/Downloads/chromedriver")

driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#locator ID,Xpath,Classname , name ,linkText
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")

driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")

driver.find_element(By.ID,"exampleCheck1").click()  

# Xpath   -        //tagname[@attribute='value'] -> //input[@type="submit"]
# CSSselector -   tagname[attribute='value'] -> input[@type="submit"] #ID , .classname
driver.find_element(By.CSS_SELECTOR,"input[value='Submit'").click()
# driver.find_element(By.XPATH,'//input[@type="submit"]').click()
#static dropdown
dropdown =Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.deselect_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.deselect_by_index(0)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
submit_message =driver.find_element(By.CLASS_NAME, 'alert-success').text
print(submit_message)
assert "Success" in submit_message
