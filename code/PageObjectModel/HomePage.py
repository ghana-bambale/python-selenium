from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = "twotabsearchtextbox"
        self.search_button = "nav-search-submit-button"
        self.search_results_section = "//div[@class='a-section a-spacing-small a-spacing-top-small']"
        self.search_reults_list = "//div[@data-component-type='s-search-result']//child::span[@class='a-size-medium a-color-base a-text-normal']"

    def search_for_product(self, search_product):
        self.driver.find_element_by_id(self.search_box).send_keys(search_product)
        self.driver.find_element_by_id(self.search_button).click()

    def check_results_click_product(self, product_to_find):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.search_results_section)))
        self.original_window = self.driver.current_window_handle
        assert self.driver.window_handles == 1

        for item in self.search_reults_list:
            product_name_from_list = item.text
            if product_name_from_list.find(product_to_find):
                item.click()
                print("Item was found and clicked")
        