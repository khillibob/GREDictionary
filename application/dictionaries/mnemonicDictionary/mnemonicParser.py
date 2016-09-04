import application.dictionaries.mnemonicDictionary.mnemonicData as mnemonicData
import json
import application.Utils.UIUtils.seleniumutils as seleniumUtils
import application.config as config
import os
import application.Utils.dbUtil.dbUtils as dbUtils
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
        tables = dbUtils.DBUtil().getAllTablenames()
        print(tables)
        words = dbUtils.DBUtil().getAllWords(table_name)
        print(len(words))
        return words
    
    
    def getEasyMeanings(self,word,webdriver):
        """
        definition    :    This method will extract the easy remember technique from Mnemonic 
        input         :    input will be the word and the webdriver
        output        :    Output will be the dictionary of techniques
                            Structure:
                            result['word'] = ['meaning1','meaning2']
        """
        SECTION_CSS_SELECTOR = "#home-middle-content > div:nth-child(5)"
        #a = seleniumUtils.SeleniumUtils(BASE_URL+alphbt)
        BASE_URL = "http://www.mnemonicdictionary.com/?word="
         
         
MnemonicParser().getEasyMeanings('a',None)            