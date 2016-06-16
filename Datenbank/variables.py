# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 10:12:11 2016

@author: Joachim
"""
data2 = 5
data3 = 5
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def dynamic_data_entry():
    
    c.execute("INSERT INTO test (b, c) VALUES (?, ?)", (data2, data3))
    conn.commit()

dynamic_data_entry()
c.close()
conn.close()

