import os,pdb,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumUtils():
    def __init__(self,url):
        if os.name=="nt":
            chromedriver = os.path.dirname(__file__)+os.sep+'chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        
        self.chrome_options.add_experimental_option("debuggerAddress", url)
        self.webDriver = webdriver.Chrome(chromedriver, chrome_options=self.chrome_options)
        self.webDriver.implicitly_wait(20) 

    
        
    def close(self):
        try:
            self.webDriver.quit()
            self.webDriver = None
        except Exception :
            print ( Exception.__cause__)
    