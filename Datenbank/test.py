# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:39:46 2016

@author: Joachim
"""

import sqlite3
conn = sqlite3.connect('testmest.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS 'testtable' (\
    `a`	INTEGER,\
    `b`	INTEGER,\
    `c`	INTEGER,\
    `d`	INTEGER\
    );"
    
    
    )

def data_entry():
    c.execute("INSERT INTO testtable VALUES(1, 2, 3, 4)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()