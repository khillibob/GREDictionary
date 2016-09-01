import application.dictionaries.magoosh.magooshData as magooshData
import json
import application.Utils.UIUtils.seleniumutils as seleniumUtils
import application.config as config
import os
#config.seleniumObj = seleniumUtils.SeleniumUtils()



CHECHEK_NEWWORD_STATUS_CSS = ".label.label-flashcard"

MAGOOSH_WORD_OUTER_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.front.card.flashcard-card > a:nth-child(1) > div > h1"
MAGOOSH_GET_MEANING_LINK_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.front.card.flashcard-card > a.card-footer.text-center"

WORD_STATUS_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.front.card.flashcard-card > a:nth-child(1) > div > div"

WORD_NAME_CSS_Selector = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > div > h3"
WORD_MEANING_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > div > div:nth-child(3) > p"
WORD_SENTENCES_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > div > em > p"
WORD_EXTRA_NOTE_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > div > div.flashcard-note"
WORD_NEXT_WORD_CSS_SELECTOR = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > a.card-footer.card-footer-success.text-center"

WORD_DETAILS = "body > div.container.u-margin-T-xl > div > div > div.flashcard-container.u-margin-V-m > div > div.back.card.flashcard-card > div"

class MagooshUtil():
    
    def getAdvancedWords(self):
        #getting the word
        wordDict ={}
        wordDetails ={}
        wordDict.clear()
        advanced_links = magooshData.MAGOOSH_ADVANCED_LINKS
        for link in advanced_links:
            a = seleniumUtils.SeleniumUtils(magooshData.MAGOOSH_BASE_URL+link)
        
            wordDict ={}
            wordDetails ={}
            wordDict.clear()
            while(len(wordDict)<51): 
                wordDetails = {}
                word = a.getText_by_css_selector(MAGOOSH_WORD_OUTER_CSS_SELECTOR)
                word_status = a.getText_by_css_selector(WORD_STATUS_CSS_SELECTOR)
                if len(wordDict)>= 49 and  "new word" not in word_status.lower():
                    break
                link_page_element = a.find_element_by_css_selector(MAGOOSH_GET_MEANING_LINK_CSS_SELECTOR)
                wordDetails["wordURL"] = a.get_Attribute_by_Element(elem=link_page_element,attribName='href')
                a.clickElem(link_page_element)
                
                word_org = a.getText_by_css_selector(WORD_NAME_CSS_Selector)
                #word_content = a.find_element_by_css_selector(WORD_DETAILS)
                word_meanings = a.find_elements_by_class_name("flashcard-text")
                word_sentences = a.find_elements_by_class_name("flashcard-example")
                count = 1;
                for se in word_meanings:
                    wordDetails["meaning_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                count=1
                for se in word_sentences:
                    wordDetails["sentence_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                #word_meaning = a.getText_by_css_selector(WORD_MEANING_CSS_SELECTOR)
                #word_sentence = a.getText_by_css_selector(WORD_SENTENCES_CSS_SELECTOR)
                word_extra_note = a.getText_by_css_selector(WORD_EXTRA_NOTE_CSS_SELECTOR)
                wordDetails["word"] = word_org
                #wordDetails["wordMeaning"] = word_meaning
                #wordDetails["wordSentence"] = word_sentence
                wordDetails["wordExtraNote"] = word_extra_note
                # a.current_url()
                """    
                print(wordDetails)
                print(word_org)
                print(word_meaning)
                print(word_sentence)
                print(word_extra_note)
                """    
                wordDict[word_org] = wordDetails
                #print(wordDetails)
                print (len(wordDict))
                self.writeToJson(wordDict,link.split('/')[4]+'.json','ADVANCED')
                a.clickElem(a.find_element_by_css_selector(WORD_NEXT_WORD_CSS_SELECTOR))
                
            a.quit()
    
    def getCommonWords(self):
        #getting the word
        wordDict ={}
        wordDetails ={}
        wordDict.clear()
        links = magooshData.MAGOOSH_COMMON_LINK
        for link in links:
            a = seleniumUtils.SeleniumUtils(magooshData.MAGOOSH_BASE_URL+link)
        
            wordDict ={}
            wordDetails ={}
            wordDict.clear()
            while(len(wordDict)<51): 
                wordDetails = {}
                word = a.getText_by_css_selector(MAGOOSH_WORD_OUTER_CSS_SELECTOR)
                word_status = a.getText_by_css_selector(WORD_STATUS_CSS_SELECTOR)
                if len(wordDict)>= 49 and  "new word" not in word_status.lower():
                    break
                link_page_element = a.find_element_by_css_selector(MAGOOSH_GET_MEANING_LINK_CSS_SELECTOR)
                wordDetails["wordURL"] = a.get_Attribute_by_Element(elem=link_page_element,attribName='href')
                a.clickElem(link_page_element)
                
                word_org = a.getText_by_css_selector(WORD_NAME_CSS_Selector)
                #word_content = a.find_element_by_css_selector(WORD_DETAILS)
                word_meanings = a.find_elements_by_class_name("flashcard-text")
                word_sentences = a.find_elements_by_class_name("flashcard-example")
                count = 1;
                for se in word_meanings:
                    wordDetails["meaning_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                count=1
                for se in word_sentences:
                    wordDetails["sentence_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                #word_meaning = a.getText_by_css_selector(WORD_MEANING_CSS_SELECTOR)
                #word_sentence = a.getText_by_css_selector(WORD_SENTENCES_CSS_SELECTOR)
                word_extra_note = a.getText_by_css_selector(WORD_EXTRA_NOTE_CSS_SELECTOR)
                wordDetails["word"] = word_org
                #wordDetails["wordMeaning"] = word_meaning
                #wordDetails["wordSentence"] = word_sentence
                wordDetails["wordExtraNote"] = word_extra_note
                # a.current_url()
                """    
                print(wordDetails)
                print(word_org)
                print(word_meaning)
                print(word_sentence)
                print(word_extra_note)
                """    
                wordDict[word_org] = wordDetails
                #print(wordDetails)
                print (len(wordDict))
                self.writeToJson(wordDict,link.split('/')[4]+'.json','COMMONS')
                a.clickElem(a.find_element_by_css_selector(WORD_NEXT_WORD_CSS_SELECTOR))
                
            a.quit()
    def getBasicWords(self):
        #getting the word
        wordDict ={}
        wordDetails ={}
        wordDict.clear()
        links = magooshData.MAGOOSH_BASIC_LINKS
        for link in links:
            a = seleniumUtils.SeleniumUtils(magooshData.MAGOOSH_BASE_URL+link)
        
            wordDict ={}
            wordDetails ={}
            wordDict.clear()
            while(len(wordDict)<51): 
                wordDetails = {}
                word = a.getText_by_css_selector(MAGOOSH_WORD_OUTER_CSS_SELECTOR)
                word_status = a.getText_by_css_selector(WORD_STATUS_CSS_SELECTOR)
                if len(wordDict)>= 49 and "new word" not in word_status.lower():
                    break
                link_page_element = a.find_element_by_css_selector(MAGOOSH_GET_MEANING_LINK_CSS_SELECTOR)
                wordDetails["wordURL"] = a.get_Attribute_by_Element(elem=link_page_element,attribName='href')
                a.clickElem(link_page_element)
                
                word_org = a.getText_by_css_selector(WORD_NAME_CSS_Selector)
                #word_content = a.find_element_by_css_selector(WORD_DETAILS)
                word_meanings = a.find_elements_by_class_name("flashcard-text")
                word_sentences = a.find_elements_by_class_name("flashcard-example")
                count = 1;
                for se in word_meanings:
                    wordDetails["meaning_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                count=1
                for se in word_sentences:
                    wordDetails["sentence_"+str(count)] = a.getText_by_Elem(se)
                    count = count+1
                #word_meaning = a.getText_by_css_selector(WORD_MEANING_CSS_SELECTOR)
                #word_sentence = a.getText_by_css_selector(WORD_SENTENCES_CSS_SELECTOR)
                word_extra_note = a.getText_by_css_selector(WORD_EXTRA_NOTE_CSS_SELECTOR)
                wordDetails["word"] = word_org
                #wordDetails["wordMeaning"] = word_meaning
                #wordDetails["wordSentence"] = word_sentence
                wordDetails["wordExtraNote"] = word_extra_note
                # a.current_url()
                """    
                print(wordDetails)
                print(word_org)
                print(word_meaning)
                print(word_sentence)
                print(word_extra_note)
                """    
                wordDict[word_org] = wordDetails
                #print(wordDetails)
                print (len(wordDict))
                self.writeToJson(wordDict,link.split('/')[4]+'.json','BASIC')
                a.clickElem(a.find_element_by_css_selector(WORD_NEXT_WORD_CSS_SELECTOR))
                
            a.quit()
    
    def writeToJson(self,wordDictionary,jsonName,difficulty):
        jsonFolder = os.path.join(os.path.dirname(__file__),difficulty)
        if not os.path.exists(jsonFolder):
            os.makedirs(jsonFolder)
        jsonFile = os.path.join(jsonFolder,jsonName)
        
        with open(jsonFile, 'w+') as outfile:
            json.dump(wordDictionary, outfile)
    
MagooshUtil().getAdvancedWords()
MagooshUtil().getCommonWords()
MagooshUtil().getBasicWords()
