from selenium import webdriver
#driver = webdriver.Firefox(executable_path="/home/thebadcoder/MyWorkSpace/Testing/python_selenium/code/drivers/geckodriver-v0.29.1-linux32/geckodriver")
driver = webdriver.Firefox()
driver.get("https://www.amazon.in")


## Validation
page_title = driver.title
print("Page title: ",page_title)

## input something
search_for = "OnePlus Nord CE 5G"

search_box = driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]')
search_box.send_keys(search_for)

## click something
search_button = driver.find_element_by_id("nav-search-submit-button")
search_button.click()

print("Automation completed")
driver.close()
