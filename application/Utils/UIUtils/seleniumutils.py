import os,pdb,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



import os,pdb,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

RETRY=2

class SeleniumUtils():

    def __init__(self,url):
        if os.name=="nt":
            chromedriver = os.path.dirname(__file__)+os.sep+'chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--incognito")
        self.webDriver = webdriver.Chrome(chromedriver,chrome_options = self.chrome_options)
        self.webDriver.get(url)
        self.webDriver.implicitly_wait(5) 
        
    def getWebDriver(self):
        return self.webDriver
    def switch_to_window(self,handleStr):
        time.sleep(1)
        handles = self.webDriver.window_handles
        for handle in handles:
            self.webDriver.switch_to_window(handle)
            windowTitle = self.webDriver.title
            if windowTitle.find(handleStr) !=-1:
                return True
            else:
                return False
        
    def clickElem(self,elem,retries=RETRY):
        counter=0
        time.sleep(1)
        while(counter<retries):
            try:
                if elem.is_displayed():
                    elem.click()
                    return True
                else:
                    return False
            except StaleElementReferenceException:
                return False
            except Exception:
                counter+=1
        return False        
        
    def find_element_by_tag_name(self,name,driver=None,retries=RETRY):
        counter=0
        while(counter<retries):
            try:
                
                time.sleep(1)
                if driver:
                    return driver.find_element_by_tag_name(name)
                else:
                    return self.webDriver.find_element_by_tag_name(name)
            except StaleElementReferenceException:
                return None        
            except Exception:
                time.sleep(1)
                counter+=1
        return None       
    
             
    def find_elements_by_tag_name(self,name,driver=None,retries=RETRY):
        counter=0
        while(counter<retries):
            try:
                time.sleep(1)
                if driver:
                    return driver.find_elements_by_tag_name(name)
                else:
                    return self.webDriver.find_elements_by_tag_name(name)
            except StaleElementReferenceException:
                return None        
            except Exception:
                time.sleep(1)
                counter+=1
        return None                

  
    def find_and_click_element_by_css_selector(self,CSSStr,driver=None,retries=RETRY):
        counter=0
        while(counter<retries):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if elem.is_displayed():
                    elem.click()
                    return True
                else:
                    return False
            except StaleElementReferenceException:
                return None        
            except Exception:
                counter+=1
        return False
    def find_element_by_css_selector(self,CSSStr,driver=None,retries=RETRY):
        counter=0
        while(counter<retries):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                return elem
            except StaleElementReferenceException:
                return None        
            except Exception:
                counter+=1
        return False
    
    def sendKeysByCSS(self,CSSStr,dataStr):
        elem=self.webDriver.find_element_by_css_selector(CSSStr).send_keys(dataStr)
        return True
    
    def sendKeys(self,dataStr,driver):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.send_keys(dataStr)
                    return True
            except StaleElementReferenceException:
                return None
            except Exception as e:
                counter+=1
    
    def sendEnterKeyByCSS(self,CSSStr):
        try:
            time.sleep(1)
            return self.getElemByCSS(CSSStr).send_keys(Keys.RETURN)
        except Exception:
            print("Error")
        
    def find_element_by_id(self,id):
        return self.webDriver.find_element_by_id(id)

    def find_element_by_css_selector_classID(self,classID,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                
                time.sleep(1)
                if driver:
                    return driver.find_element_by_css_selector(classID)
                else:    
                    return self.webDriver.find_element_by_css_selector(classID)
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None

    def find_elements_by_css_selector_classID(self,classID,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    return driver.find_elements_by_css_selector(classID)
                else:    
                    return self.webDriver.find_elements_by_css_selector(classID)
                
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None
    
    def getActionChain(self):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                return ActionChains(self.webDriver)
                
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None
    
    def move_to_element(self,actionChain,elem):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                return actionChain.move_to_element(elem)
                
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None
    
    def perform(self,actionChain):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                return actionChain.perform()
                
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None
    
    def find_elements_by_class_name(self,classID,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    return driver.find_elements_by_class_name(classID)
                else:    
                    return self.webDriver.find_elements_by_class_name(classID)
                
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None
                    
    def find_element_by_class_name(self,classID,driver=None):
        
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    return driver.find_element_by_class_name(classID)
                else:    
                    return self.webDriver.find_element_by_class_name(classID)
            except StaleElementReferenceException:
                return None
            except Exception:
                counter+=1
        return None

    def getText_by_css_selector(self,CSSStr,driver=None):
        counter=0
        retText=None
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if elem.is_displayed():
                    retText =elem.text
                    break
            except NoSuchElementException:
                return None
                print("Error")
            except StaleElementReferenceException:
                return None
            except Exception:
                print("Error")
            counter+=1
        return retText       
            
    def getText_by_Elem(self,elem):
        try:
            time.sleep(1)
            return elem.text
        
        except StaleElementReferenceException:
            return None
        except Exception:
            return None
        
    def getDisplayStatus(self,elem):
        try:
            time.sleep(1)
            return elem.is_displayed()
        except StaleElementReferenceException:
            return None
        except Exception:
            return None    
    def getDisplayStatusByCSS(self,CSSStr,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if elem.is_displayed():
                    return True
            except NoSuchElementException:
                print ("no such element ")
            except StaleElementReferenceException:
                return None
            except Exception:
                print ("inside exception getDisplayStatusCSS ")
            counter+=1
        return False 
    
    def isEnabledStatusByCSS(self,CSSStr,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if elem.is_enabled():
                    return True
            except NoSuchElementException:
                print( "no such element "+ CSSStr)
            except StaleElementReferenceException:
                return None
            except Exception:
                print ("inside exception getEnabledStatusByCSS ") 
            counter+=1
        return False 
    
    def clear_by_css_selector(self,CSSStr,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if elem.clear():
                    return True
            except StaleElementReferenceException:
                return None
            except NoSuchElementException:
                print( "NoSuchElementException")
            except Exception:
                print( "inside exception clearByCSS ")
            counter+=1
        return False 
    
    def execute_js_script(self,script,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    return driver.execute_script(script)
                else:
                    return self.webDriver.execute_script(script)
            except StaleElementReferenceException:
                return None        
            except Exception:
                time.sleep(2)
                counter+=1
        return None 
    
    def getCheckBoxStatusByName(self,name,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_name(name)
                else:
                    elem=self.webDriver.find_element_by_name(name)
                if elem.is_selected():
                    return True
            except NoSuchElementException:
                print ("no such element ")
            except StaleElementReferenceException:
                return None
            except Exception:
                print ("inside exception getDisplayStatusCSS ") 
            counter+=1
        return False  
    
    def getActiveClassStatusByCSS(self,CSSStr,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                print ("inside getActiveClassStatusByCSS "+CSSStr)
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                if 'active' in elem.get_attribute("class"):
                    return True
            except NoSuchElementException:
                print ("no such element "+ CSSStr)
            except StaleElementReferenceException:
                return None
            except Exception:
                print ("inside exception getActiveClassStatusByCSS ") 
            counter+=1
        return False
#    self.webDriver.
    def getAttributeByCSS(self,CSSStr,attribute,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    elem=driver.find_element_by_css_selector(CSSStr)
                else:
                    elem=self.webDriver.find_element_by_css_selector(CSSStr)
                return elem.get_attribute(attribute)
            except Exception:
                print("Exception")
            counter+=1
        return None  
    
    def switchToFrame(self,driver):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                return self.webDriver.switch_to_frame(driver)
            except Exception:
                print("inside exception switchToFrame ") 
            counter+=1
        return False
    
    def switchToDefaultContent(self,driver=None):
        counter=0
        while(counter<RETRY):
            try:
                time.sleep(1)
                if driver:
                    return driver.switch_to_default_content()
                else:
                    return self.webDriver.switch_to_default_content()
            except Exception:
                print ("inside exception switchToDefaultContent ")
            counter+=1
        return False
        
    def quit(self):
        try:
            self.webDriver.quit()
            self.webDriver = None
        except Exception:
            print ("in exception quit webdriver")
    
    def back(self):
        """
        Goes one step backward in the browser history.
        """
        try:
            self.webDriver.back()
            self.webDriver = None
        except Exception:
            print ("in exception back")
    
    def current_url(self):
        try:
            return self.webDriver.current_url
        except Exception:
            print ("in exception")
    def get_Attribute_by_Element(self,elem,attribName):
        return elem.get_attribute(attribName)
    def find_element_by_link_text(self,link_text):
        try:
            self.webDriver.find_element_by_link_text(link_text)
            self.webDriver = None
        except Exception:
            print ("in exception")
    def find_element_by_xpath(self,xpath):
        try:
            return self.webDriver.find_element_by_xpath(xpath)
        except Exception:
            print ("in exception")
    def implicitly_wait(self,time_to_wait):
        try:
            self.webDriver.implicitly_wait(time_to_wait)
        except Exception:
            print ("in exception")
    def get(self,url):
        try:
            self.webDriver.get(url)
            
        except Exception:
            print ("in exception")
    
    def find_elements_by_name(self,name):
        try:
            return self.webDriver.find_elements_by_name(name)
        except Exception:
            print ("in exception")