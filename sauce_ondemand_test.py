from selenium import webdriver
import unittest, time, re
import os
import json

from ParseSauceURL import *
from SeleniumFactory import *

"""
"""
class testSauceWrappers(unittest.TestCase):


    def retrieve_job_details(self, browser):
        sauceRest = SauceRest(self.username, self.access_key)
        result = sauceRest.get(browser.id())
        data = json.loads(result)
        return data

    def test_webdriver_success(self):

        browser = SeleniumFactory().createWebDriver()
        browser.get("http://amazon.com")
        assert "Amazon.com" in browser.title
        browser.job_passed()
        data = self.retrieve_job_details(browser)
        assert data['passed']
        browser.quit()

    def test_webdriver_failed(self):

        browser = SeleniumFactory().createWebDriver()
        browser.get("http://amazon.com")
        assert "Amazon.com" in browser.title
        browser.job_failed()
        data = self.retrieve_job_details(browser)
        assert not data['passed']
        browser.quit()

if __name__ == "__main__":
    unittest.main()