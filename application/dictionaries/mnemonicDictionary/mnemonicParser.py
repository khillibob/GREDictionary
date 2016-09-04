import application.dictionaries.mnemonicDictionary.mnemonicData as mnemonicData
import json
import application.Utils.UIUtils.seleniumutils as seleniumUtils
import application.config as config
import os
import application.Utils.dbUtil.dbUtils as dbUtils
import traceback

import urllib
from bs4 import BeautifulSoup


class MnemonicParser():
    
    
    def getAlphabetPages(self):
        # incomplete
        BASE_URL = mnemonicData.MNEMONIC_ALPHABET_BASE_URL
        alphbt = 'A'
        a = seleniumUtils.SeleniumUtils(BASE_URL+alphbt)
        page_count_mnemonic={}
        while ord(alphbt)<=ord('Z'):
            a.get(BASE_URL+alphbt)
            page_count_element = (a.find_element_by_css_selector(mnemonicData.MNEMONIC_PAGE_COUNT_CSS_SELECTOR)).find_elements_by_tag_name("li")
            print(alphbt)
            print(len(page_count_element))
            page_count_mnemonic[alphbt] = len(page_count_element)
            alphbt = chr(ord(alphbt)+1)
        print(page_count_mnemonic)
        
    def fetchAllWords(self):
        
        """
        
        def:    get all words from table
        input:    None
        output:    returns all words list
        
        """
        
        table_name = 'MNEMONIC_DICT'
        dbName = 'C:\\HDD\\Subhendu\\ProjectX\\GREX\\GRE.db'
        tables = dbUtils.DBUtil().getAllTablenames(dbName)
        print(tables)
        words = dbUtils.DBUtil().getAllWords(table_name,dbName)
        print(len(words))
        return words
    
    
    def getEasyMeanings(self,word):
        """
        definition    :    This method will extract the easy remember technique from Mnemonic 
        input         :    input will be the word and the webdriver
        output        :    Output will be the dictionary of techniques
                            Structure:
                            result['word'] = ['meaning1','meaning2']
        """
        
        try:
            SECTION_CSS_SELECTOR = "#home-middle-content div:nth-child(5)"
            #a = seleniumUtils.SeleniumUtils(BASE_URL+alphbt)
            BASE_URL = "http://www.mnemonicdictionary.com/?word="
            page = urllib.request.urlopen(BASE_URL + word).read()
            soup = BeautifulSoup(page, "html.parser")
            #page = urllib2.urlopen('http://yahoo.com').read()
            #soup = BeautifulSoup(page)
            #sub_page = str(soup.select(SECTION_CSS_SELECTOR))
            soup = BeautifulSoup(page, "html.parser")
            divs = soup.find_all("div", attrs={"class": "span9"})
            print(len(divs))
            print(divs[0].get_text().strip())
            if(len(divs)>=2):
                a='a'
        except Exception:
            traceback.print_exc()
    
    
    
    def insertMnemonic(self):
        
        
        dbname = 'C:\\HDD\\Subhendu\\ProjectX\\GREX\\GRE.db'
        words = MnemonicParser().fetchAllWords(dbname)
        for word in words:
            meanings = self.getEasyMeanings(word)
            if len(meanings)>=2:
                dbUtils.DBUtil().updateMnemonic(word, meanings[0], meanings[1],dbname)
            elif len(meanings)==1:
                dbUtils.DBUtil().updateMnemonic(word, meanings[0], 'None',dbname)
            else:
                dbUtils.DBUtil().updateMnemonic(word, 'None', 'None',dbname)
MnemonicParser().insertMnemonic()
#MnemonicParser().getEasyMeanings('pedestrian')            