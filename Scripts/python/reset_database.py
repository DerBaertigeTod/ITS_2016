# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 21:19:10 2016

@author: Joachim
"""
#set all to 20
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def del_and_update():
    c.execute('UPDATE color SET rock= 20')
    c.execute('UPDATE color SET pop= 20')
    c.execute('UPDATE color SET hiphop= 20')
    c.execute('UPDATE color SET metal= 20')
    c.execute('UPDATE color SET reggae= 20')
    conn.commit()
    
del_and_update()
c.close()
conn.close()

#set musikdateipfad

import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def pfad():
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    conn.commit()
    
pfad()
c.close()
conn.close()