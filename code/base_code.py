from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox(executable_path="/home/thebadcoder/MyWorkSpace/Testing/python_selenium/code/drivers/geckodriver-v0.29.1-linux32/geckodriver")
driver = webdriver.Firefox()
url = "https://www.amazon.in"
driver.get(url)

#Set Wait for later
wait =  WebDriverWait(driver, 10)

## Validation
page_title = driver.title
print("Page title: ",page_title)

## input something
search_for_product = "OnePlus Nord CE 5G"

search_box = driver.find_element_by_xpath('//input[@id="twotabsearchtextbox"]')
search_box.send_keys(search_for_product)

## click something
search_button = driver.find_element_by_id("nav-search-submit-button")
search_button.click()

## Wait for Search results
wait_for_serch_element = "a-section a-spacing-small a-spacing-top-small"
try:
    element_to_expect = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='a-section a-spacing-small a-spacing-top-small']")))

except:
    print("There was an exception")

## Name to check in list and click on
## OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)
expected_product_name = "OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)"
    ###################################################################
    #### A try to locate element from other element but failed  #######
    ###################################################################
    # search_products_list = driver.find_elements_by_xpath('//div[@data-component-type="s-search-result"]')
    # print("Total products returned: ",len(search_products_list))
    # for item in search_products_list:
    #     product_name_from_list = item.find_element_by_xpath("//child::span[@class='a-size-medium a-color-base a-text-normal']").text
    #     print(product_name_from_list)
    #     if product_name_from_list.find(expected_product_name) != -1:
    #         item.click()
    #         print("Element was found and clicked")

    #         try:
    #             pass
    #         except:
    #             pass

    #     else:
    #         print("No element was")

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1


search_products_list = driver.find_elements_by_xpath('//div[@data-component-type="s-search-result"]//child::span[@class="a-size-medium a-color-base a-text-normal"]')
print("Total products returned: ",len(search_products_list))
for item in search_products_list:
    product_name_from_list = item.text
    # print(product_name_from_list)                 # Was used for debug
    if product_name_from_list.find(expected_product_name) != -1:
        item.click()
        print("Element was found and clicked")
        # Wait for new window or tab to open
        wait.until(EC.number_of_windows_to_be(2))
        try:
            pass
        except:
            pass

    else:
        print("No element was found")

# Find new window / tab and switch to it
for window_item in driver.window_handles:
    if window_item != original_window:
        driver.switch_to.window(window_item)

wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='rightCol']/descendant::input[@id='add-to-cart-button']")))
add_item_to_the_cart = driver.find_element_by_xpath("//div[@id='rightCol']/descendant::input[@id='add-to-cart-button']")
add_item_to_the_cart.click()

driver.close()
driver.switch_to.window(original_window)

driver.implicitly_wait(10)
print("Automation completed")
driver.close()
