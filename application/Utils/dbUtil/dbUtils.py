import sqlite3
import os
from pprint import pprint
import json
import sys
from shutil import copyfile
from pip._vendor.distlib.compat import raw_input




class DBUtil():
    
    def createBengaliDatabse(self):
        conn = sqlite3.connect('GRE.db')
        print( "Opened database successfully")
        conn.execute('''CREATE TABLE BENGALI_DICT
                   (word CHAR(100) PRIMARY KEY     NOT NULL,
                    difficulty CHAR(20),
                    bengali_meaning CHAR(500));''')
        return conn
    def insertDataInBengaliDict(self,conn,word,diff,bengali_meaning):
        conn.execute("INSERT INTO BENGALI_DICT ("+"word"+","+"difficulty"+","+"bengali_meaning"+") VALUES (" +word+","+diff+","+bengali_meaning+")")
        conn.commit()
        
    def createMnemonicDatabase(self):
        conn = sqlite3.connect('GRE.db')
        print( "Opened database successfully")
        conn.execute('''CREATE TABLE  IF NOT EXISTS MNEMONIC_DICT
                   (word CHAR(100) PRIMARY KEY     NOT NULL,
                    way_to_remember CHAR(500),
                    way_to_remember2 CHAR(500));''')
        print("DB created")
        return conn                
    def insertMnemonic(self,conn,word,way_to_remember,way_to_remember2):
        query = "INSERT INTO MNEMONIC_DICT ("+"word"+","+"way_to_remember"+","+"way_to_remember2"+") VALUES ('" +word+"','"+way_to_remember+"','"+way_to_remember2+"')"
        print(query)
        conn.execute(query)
        conn.commit()
    
    def updateMnemonic(self,word,way_to_remember,way_to_remember2,dbName):
        conn=sqlite3.connect(dbName)
        way_to_remember = way_to_remember.replace("'","]")
        way_to_remember2 = way_to_remember2.replace("'","]")
        updateQuery = "UPDATE MNEMONIC_DICT set "+"way_to_remember = '"+way_to_remember+ "' where word='"+word+"'"
        updateQuery2 = "UPDATE MNEMONIC_DICT set "+"way_to_remember2 = '"+way_to_remember2+ "' where word='"+word+"'"
        #print(updateQuery)
        conn.execute(updateQuery)
        conn.execute(updateQuery2)
        conn.commit()
    
        
    
    def databaseClose(self,conn):
        conn.close()
    
    def insertAllWordsInDB(self,conn,tableName,path):
        for file in os.listdir(path):
            print(file)
            with open(os.path.join(path,file)) as data_file:    
                wordList = json.load(data_file)
                #print(len(wordList))
                for word, value in wordList.items():
                    print(word)
                    self.insertMnemonic(conn,word,'None','None')
                #pprint(data)
        """
        if(tableName == 'mnemonic'):
            self.insertMnemonic(conn, word, way_to_remember)
        """    
    
    def getAllTablenames(self,dbName):
        """
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        """
        
        #con = sqlite3.connect('C:\\HDD\\Subhendu\\ProjectX\\GREX\\GRE.db')
        con = sqlite3.connect(dbName)
        
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #print(cursor.fetchall())
    
    def getAllWords(self,table,dbName):
        
        """
        def:    fetch all the words from table
        input:    table name
        output:    List of words
        
        """
        
        conn = sqlite3.connect(dbName)
        query = "SELECT word from "+table
        print(query)
        cursor = conn.execute(query)
        output=[]
        for row in cursor:
            print( "word = "+  row[0])
            output.append(row[0])
        print("Operation done successfully")
        return output
    
    def moveDB(self,src,dst = "C:\\HDD\\Subhendu\\ProjectX\\GREX\\"):
        if not os.path.exists(dst):
            os.makedirs(dst)
        copyfile(src, dst)
    def createMagooshDatabase(self):
        conn = sqlite3.connect('GRE.db')
        print( "Opened database successfully")
        conn.execute('''CREATE TABLE  IF NOT EXISTS MAGOOSH_DICT
                   (word CHAR(100) PRIMARY KEY     NOT NULL,
                    wordURL CHAR(500),
                    meaning_1 CHAR(1000),
                    sentence_1 CHAR(1500),
                    meaning_2 CHAR(1000),
                    sentence_2 CHAR(1500),
                    meaning_3 CHAR(1000),
                    sentence_3 CHAR(1500),
                    way_to_remember CHAR(500),
                    way_to_remember2 CHAR(500),
                    difficulty CHAR(500));''')
        print("DB created")
        return conn

    def insertMagooshDB(self,difficulty,
                        word,
                        conn ,
                        wordURL,
                        meaning_1,
                        sentence_1,
                        meaning_2,
                        sentence_2,
                        meaning_3,
                        sentence_3,
                        way_to_remember,
                        way_to_remember2
                        ):
        query = "INSERT OR IGNORE INTO MAGOOSH_DICT ("+ \
            "word"+","+ \
            "wordURL"+","+ \
            "difficulty"+","+ \
            "meaning_1"+","+ \
            "sentence_1"+","+ \
            "meaning_2"+","+ \
            "sentence_2"+","+ \
            "meaning_3"+","+ \
            "sentence_3"+","+ \
            "way_to_remember"+","+ \
            "way_to_remember2"+") VALUES ('" \
            +word+"','"+ \
            wordURL + ','+\
            "','"+difficulty + \
            "','"+meaning_1 + \
            "','"+sentence_1 + \
            "','"+meaning_2 + \
            "','"+sentence_2 + \
            "','"+meaning_3 + \
            "','"+sentence_3 + \
            "','"+way_to_remember + \
            "','"+way_to_remember2 + \
            "')"
        print(query)
        conn.execute(query)
        conn.commit()
    
    def insertAllMagooshWords(self,path,difficulty,conn):
        for file in os.listdir(path):
            print(file)
            with open(os.path.join(path,file)) as data_file:    
                wordList = json.load(data_file)
                #print(len(wordList))
                for word, value in wordList.items():
                    print(word)
                    print(value)
                    wordURL='None'
                    meaning_1='None'
                    sentence_1='None'
                    meaning_2='None'
                    sentence_2='None'
                    meaning_3='None'
                    sentence_3='None'
                    way_to_remember='None'
                    way_to_remember2='None'
                
                    if 'wordURL' in value:
                        wordURL = value['wordURL'].replace("'","]]")
                    else:
                        wordURL = 'None'
                    
                    if 'meaning_1' in value:
                        meaning_1 = value['meaning_1'].replace("'","]]")
                    else:
                        meaning_1 = 'None'
                    
                    if 'meaning_2' in value:
                        meaning_2 = value['meaning_2'].replace("'","]]")
                    else:
                        meaning_2 = 'None'
                    
                    if 'sentence_1' in value:
                        sentence_1 = value['sentence_1'].replace("'","]]")
                    else:
                        sentence_1 = 'None'
                    
                    if 'sentence_2' in value:
                        sentence_2 = value['sentence_2'].replace("'","]]")
                    else:
                        sentence_2 = 'None'
                    
                    if 'meaning_3' in value:
                        meaning_3 = value['meaning_3'].replace("'","]]")
                    else:
                        meaning_3 = 'None'
                    
                    if 'sentence_3' in value:
                        sentence_3 = value['sentence_3'].replace("'","]]")
                    else:
                        sentence_3 = 'None'
                    
                    if 'way_to_remember' in value:
                        way_to_remember = value['way_to_remember'].replace("'","]]")
                    else:
                        way_to_remember = 'None'
                    
                    if 'way_to_remember2' in value:
                        way_to_remember2 = value['way_to_remember2'].replace("'","]]")
                    else:
                        way_to_remember2 = 'None'
                    
                    
                    self.insertMagooshDB(difficulty, word, conn, wordURL, meaning_1, sentence_1, meaning_2, sentence_2, meaning_3, sentence_3, way_to_remember, way_to_remember2)
    
    def updateMagooshDB(self,conn,word,colName,colValue):
        
        updateQuery = "UPDATE MAGOOSH_DICT set "+colName+" = '"+colValue+ "' where word='"+word+"'"
        conn.execute(updateQuery)
        conn.commit()
    
    def getDB(self,dbName):
        conn=sqlite3.connect(dbName)
        return conn
    def updateAllWayToRemember(self,conn):
        query = "SELECT word from MAGOOSH_DICT"
        print(query)
        cursor = conn.execute(query)
        for row in cursor:
            word = row[0]
            query_mnemonic = "SELECT way_to_remember,way_to_remember2 from MNEMONIC_DICT where word='"+word+"'"
            cursor_m = conn.execute(query_mnemonic)
            for row_m in cursor_m:
                way1 = row_m[0]
                way2 = row_m[1]
                self.updateMagooshDB(conn,word,'way_to_remember',way1)
                self.updateMagooshDB(conn,word,'way_to_remember2',way2)
                
            
        print("Operation done successfully")