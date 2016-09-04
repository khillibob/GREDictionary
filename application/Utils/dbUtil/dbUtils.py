import sqlite3
import os
from pprint import pprint
import json
import sys

a= "মেজাজ আচরণ ভাষা প্রভৃতির রুক্ষতা"


#print(a)

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
                    way_to_remember CHAR(500));''')
        print("DB created")
        return conn                
    def insertMnemonic(self,conn,word,way_to_remember):
        query = "INSERT INTO MNEMONIC_DICT ("+"word"+","+"way_to_remember"+") VALUES ('" +word+"','"+way_to_remember+"')"
        print(query)
        conn.execute(query)
        conn.commit()
    
    def updateMnemonic(self,conn,word,way_to_remember):
        updateQuery = "UPDATE MNEMONIC_DICT set "+"way_to_remember = '"+way_to_remember+ "' where word='"+word+"'"
        print(updateQuery)
        conn.execute(updateQuery)
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
                    self.insertMnemonic(conn,word,'None')
                #pprint(data)
        """
        if(tableName == 'mnemonic'):
            self.insertMnemonic(conn, word, way_to_remember)
        """    
    
    def getAllTablenames(self):
        """
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        """
        
        con = sqlite3.connect('C:\\HDD\\Subhendu\\ProjectX\\GREX\\GRE.db')
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #print(cursor.fetchall())
    
    def getAllWords(self,table):
        """
        def:    fetch all the words from table
        input:    table name
        output:    List of words
        
        """
        conn = sqlite3.connect('C:\\HDD\\Subhendu\\ProjectX\\GREX\\GRE.db')
        query = "SELECT word from "+table
        print(query)
        cursor = conn.execute(query)
        output=[]
        for row in cursor:
            print( "word = "+  row[0])
            output.append(row[0])
        print("Operation done successfully")
        return output
    