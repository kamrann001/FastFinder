from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PATH = "C:\Program Files (x86)\chromedriver.exe"

class Driver:
    def __init__(self, headless):
        self.headless = headless
        self.options = Options()
        self.options.headless = self.headless
        self.driver = webdriver.Chrome(executable_path=PATH, options=self.options)


    def get_driver(self):
        return self.driver
