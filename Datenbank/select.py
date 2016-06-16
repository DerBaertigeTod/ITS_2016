# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 21:19:10 2016

@author: Joachim
"""

import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def read_from_db():
    
   c.execute('SELECT prozent FROM g where id=1 ')
   data = c.fetch()
   conn.commit()
   
    
c.close()
conn.close()