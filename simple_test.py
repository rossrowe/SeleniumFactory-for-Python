from selenium import webdriver
import unittest, time, re
import os

from ParseSauceURL import *
from SeleniumFactory import *

class testParseSauceURL(unittest.TestCase):
	def setUp(self):
		self.url = "sauce-ondemand:?username=rossco_9_9&access-key=44f0744c-1689-4418-af63-560303cbb37b&job-name=simple test&os=Linux&browser=firefox&browser-version=7&firefox-profile-url=&max-duration=300&idle-timeout=90&user-extensions-url="

	def test_parse(self):
		parse = ParseSauceURL(self.url)
		self.assertEqual("simple test", parse.getJobName())
		self.assertEqual("Linux", parse.getOS())
		self.assertEqual("firefox", parse.getBrowser())
		self.assertEqual("7", parse.getBrowserVersion())
		self.assertEqual("", parse.getFirefoxProfileURL())
		self.assertEqual(300, parse.getMaxDuration())
		self.assertEqual(90, parse.getIdleTimeout())
		self.assertEqual("", parse.getUserExtensionsURL())



class testSelenium2(unittest.TestCase):
    def setUp(self):
    	self.browser = SeleniumFactory().createWebDriver()
    					
    def test_get(self):
      	self.browser.get("http://amazon.com")
        assert "Amazon.com" in self.browser.title
    
    def tearDown(self):
    	self.browser.quit()
    	
 
class testSelenium1(unittest.TestCase):
    def setUp(self):
    	self.browser = SeleniumFactory().create()
    					
    def test_open(self):
      	self.browser.open("http://amazon.com")
        assert "Amazon.com" in self.browser.get_title()
    
    def tearDown(self):
    	self.browser.stop()
    	

if __name__ == "__main__":
    unittest.main()
