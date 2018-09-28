
"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

siteURL = 'http://site:8050'
apiURL = 'http://api:80/users'

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Fill Out Form Completely and Click Submit"""
        try:
            self.driver.get(siteURL)
            el = self.driver.find_element_by_id("username")
            el.click()
            el.send_keys("test1Username")
            
            el = self.driver.find_element_by_id("email")
            el.send_keys("test1Email@gmail.com")
            
            el = self.driver.find_element_by_id("address")
            el.send_keys("test1Address")

            el = self.driver.find_element_by_id("birthday")
            el.send_keys("1/1/1970")

            el = self.driver.find_element_by_id("button")
            el.click()

#            screenshot = self.driver.get_screenshot_as_png()
#            self.driver.save_screenshot("test.png")
        except NoSuchElementException as ex:
            self.driver.save_screenshot("test_1_fail.png")
            self.fail(ex.msg)
    def test_case_2(self):
        """Verify That Results from above test are Present In Table"""
        try:
            self.driver.get(siteURL)
            rows = self.driver.find_elements_by_tag_name("tr")
            l = []
            for row in rows:
                text = row.text
                l.append(text)
            #Entry Inserted In Test 1
            prev = "test1Address 1/1/1970 test1Email@gmail.com test1Username"
            self.assertIn(prev,l)
        except NoSuchElementException as ex:
            self.driver.save_screenshot("test_2_fail.png")
            self.fail(ex.msg)
    def test_case_3(self):
        """API POST Test: Success"""
        import requests
        data = {
            "username": "test3Username",
            "email": "test3Email@gmail.com",
            "address": "test3Address",
            "birthday": "1/1/1970",
        }
        response = requests.post(apiURL, json=data)
        self.assertLess(response.status_code, 400)
    def test_case_4(self):
        """API GET Test: Success"""
        import requests
        data = {
            "username": "test3Username",
            "email": "test3Email@gmail.com",
            "address": "test3Address",
            "birthday": "1/1/1970",
        }
        response = requests.get(apiURL)
        self.assertEqual(response.status_code, 200)
        l =  response.json()["data"]
        self.assertIn(data,l)
    def test_case_5(self):
        """API POST Test: Fail"""
        import requests
        data = {
            "username": "test5Username",
            "email": "test5Email@gmail.com",
            "address": "test5Address",
        }
        response = requests.post(apiURL, json=data)
        self.assertEqual(response.status_code, 400)
    def test_case_6(self):
        """API GET Test: Fail"""
        import requests
        data = {
            "username": "test5Username",
            "email": "test5Email@gmail.com",
            "address": "test5Address",
        }
        response = requests.get(apiURL)
        self.assertEqual(response.status_code, 200)
        l =  response.json()["data"]
        self.assertNotIn(data,l)

    def test_case_7(self):
        """Fill Out Form Incompletely and Click Submit"""
        try:
            self.driver.get(siteURL)
            el = self.driver.find_element_by_id("username")
            el.click()
            el.send_keys("test7Username")
            
            el = self.driver.find_element_by_id("email")
            el.send_keys("test7Email@gmail.com")
            
            el = self.driver.find_element_by_id("address")
            el.send_keys("test7Address")

            el = self.driver.find_element_by_id("button")
            el.click()

#            screenshot = self.driver.get_screenshot_as_png()
#            self.driver.save_screenshot("test.png")
        except NoSuchElementException as ex:
            self.driver.save_screenshot("test_7_fail.png")
            self.fail(ex.msg)
    def test_case_8(self):
        """Verify That Results from above test are Present In Table"""
        try:
            self.driver.get(siteURL)
            rows = self.driver.find_elements_by_tag_name("tr")
            l = []
            for row in rows:
                text = row.text
                l.append(text)
            #Entry Inserted In Test 1
            prev = "test7Address test7Email@gmail.com test7Username"
            self.assertNotIn (prev,l)
        except NoSuchElementException as ex:
            self.driver.save_screenshot("test_8_fail.png")
            self.fail(ex.msg)
if __name__ == '__main__':
    time.sleep(2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=3).run(suite)
