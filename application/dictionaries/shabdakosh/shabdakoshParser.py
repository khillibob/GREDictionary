import json
import application.Utils.UIUtils.seleniumutils as seleniumUtils
import application.config as config
import os
from bs4 import BeautifulSoup
import re


BASE_URL = "http://www.shabdkosh.com/bn/browse"
CSS_FOR_ALPHABET = "#content > div:nth-child(2) > div.col-lg-4.col-md-5 > a:nth-child(2)"

class shabdakoshUtil():
    SEARCH_CSS = "#e"
    RESULT_DIV_CSS_SELECTOR = "#left > div.row > div"
    POS_SELECTOR = "#left > div.row > div > h3"
    MEANING_CSS = "#left > div.row > div > ol"
    
    #parser = seleniumUtils.SeleniumUtils(BASE_URL)
    pages = {}
    pages['a'] = 10
    pages['b'] = 8
    pages['c'] = 14
    pages['d'] = 9
    pages['e'] = 7
    pages['f'] = 8
    pages['g'] = 6
    pages['h'] = 6
    pages['i'] = 9
    pages['j'] = 2
    pages['k'] = 2
    pages['l'] = 6
    pages['m'] = 8
    pages['n'] = 4
    pages['o'] = 4
    pages['p'] = 12
    pages['q'] = 1
    pages['r'] = 7
    pages['s'] = 15
    pages['t'] = 8
    pages['u'] = 5
    pages['v'] = 3
    pages['w'] = 4
    pages['x'] = 1
    pages['y'] = 1
    pages['z'] = 1
    
    
    def getMeanings(self,html_input):
        soup = BeautifulSoup(html_input,"html.parser")
        divs = soup.div.contents
        print (divs)
        print (len(divs))
        meanings = divs.ol.contents
        print (len(meanings))
        
        
    def searchWord(self,word):
        #search for the Bengali meaning of the WORD
        self.parser.sendKeysByCSS(self.SEARCH_CSS, word)
        self.par
        result_element = self.parser.find_element_by_css_selector(self.RESULT_DIV_CSS_SELECTOR)
        self.parser.find
        
    def getInfo(self,word,webdriver):
        #getting all the info of the word and return the dictionary
        print("getInfo")
input_html = '''<div class="row"><div class="col-sm-12"><h3 class="verb"><em>verb&nbsp;</em></h3><ol class="eirol"><li><i class="fa fa-volume-up fa-lg in au1" id="bn232685" title="Speak!"></i> <a class="in l" href="/bn/translate/হীন করা/হীন করা-meaning-in-Bengali-English">হীন করা</a> <span class="latin" style="display:none;">[hīna karā]</span></li><li><i class="fa fa-volume-up fa-lg in au1" id="bn232686" title="Speak!"></i> <a class="in l" href="/bn/translate/অপমান করা/অপমান করা-meaning-in-Bengali-English">অপমান করা</a> <span class="latin" style="display:none;">[apamāna karā]</span></li><li><i class="fa fa-volume-up fa-lg in au1" id="bn232687" title="Speak!"></i> <a class="in l" href="/bn/translate/অপমানিত করা/অপমানিত করা-meaning-in-Bengali-English">অপমানিত করা</a> <span class="latin" style="display:none;">[apamānita karā]</span></li><li><i class="fa fa-volume-up fa-lg in au1" id="bn232688" title="Speak!"></i> <a class="in l" href="/bn/translate/মানহানি করা/মানহানি করা-meaning-in-Bengali-English">মানহানি করা</a> <span class="latin" style="display:none;">[mānahāni karā]</span></li></ol></div></div>'''
shabdakoshUtil().getMeanings(input_html)