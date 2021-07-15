from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.HomePage import HomePage
import unittest

class GeneralUITests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = webdriver.Firefox(executable_path="/home/thebadcoder/MyWorkSpace/Testing/python_selenium/code/drivers/geckodriver-v0.29.1-linux32/geckodriver")
        cls.driver = webdriver.Firefox()

    

    def test_amazon(self):
        url = "https://www.amazon.in"
        self.driver.get(url)
        #Set Wait for later
        wait =  WebDriverWait(self.driver, 10)

        ## Validation
        page_title = self.driver.title
        print("Page title: ",page_title)

        ## Call POM methonds
        search_test = HomePage(self.driver)
        search_test.search_for_product(search_product="OnePlus Nord CE 5G")
        search_test.check_results_click_product(product_to_find="OnePlus Nord CE 5G (Charcoal Ink, 12GB RAM, 256GB Storage)")
        
        # Find new window / tab and switch to it
        # for window_item in self.driver.window_handles:
        #     if window_item != original_window:
        #         self.driver.switch_to.window(window_item)

        # wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='rightCol']/descendant::input[@id='add-to-cart-button']")))
        # add_item_to_the_cart = self.driver.find_element_by_xpath("//div[@id='rightCol']/descendant::input[@id='add-to-cart-button']")
        # add_item_to_the_cart.click()
        # self.driver.switch_to.window(original_window)


    def test_flipkart(self):
        self.driver.implicitly_wait(10)
        url = "https://www.flipkart.com"
        ## Flipkart for hoverover an element
        self.driver.get(url)
        close_login_popup = "//button[@class='_2KpZ6l _2doB4z']"
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,close_login_popup)))
        self.driver.find_element_by_xpath(close_login_popup).click()
        fashion_category = self.driver.find_element_by_xpath("//div[@class='eFQ30H']/descendant::div[contains(text(),'Electronics')]")
        webdriver.ActionChains(self.driver).move_to_element(fashion_category).perform()
        self.driver.execute_script ("window.scrollTo(0,250);")
        tablets_categoty = self.driver.find_element_by_xpath("//a[@class='_6WOcW9' and text()='Tablets']")
        webdriver.ActionChains(self.driver).move_to_element(tablets_categoty).perform()
        tablets_sub_category = self.driver.find_element_by_xpath("//a[@class='_6WOcW9 _3YpNQe' and text()='Tablets Without Call Facility']")
        webdriver.ActionChains(self.driver).move_to_element(tablets_sub_category).perform()
        tablets_sub_category.click()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Automation completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/thebadcoder/MyWorkSpace/Testing/python_selenium/report'))