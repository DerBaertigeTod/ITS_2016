# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 10:37:39 2016

@author: Joachim
"""
print(farbauswahl)
import sqlite3

conn = sqlite3.connect("C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db")
c = conn.cursor()

def read_from_db():
    c.execute("select * from test WHERE id=1")
    data = c.fetchall()
    print(data[0])
    
read_from_db()
c.close()
conn.close()