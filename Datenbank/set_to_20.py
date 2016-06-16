# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 21:19:10 2016

@author: Joachim
"""

import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def del_and_update():
    c.execute('UPDATE farbe SET rock= 20')
    c.execute('UPDATE farbe SET pop= 20')
    c.execute('UPDATE farbe SET hiphop= 20')
    c.execute('UPDATE farbe SET metal= 20')
    c.execute('UPDATE farbe SET reggae= 20')
    conn.commit()
    
del_and_update()
c.close()
conn.close()