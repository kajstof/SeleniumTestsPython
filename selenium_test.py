import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        submit_btn = driver.find_element_by_id("submit")
        assert "No results found." not in driver.page_source

    def test_another_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.XPATH, '//button[text()="Some text"]')

    def tearDown(self):
        self.driver.close()
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()