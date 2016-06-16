# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 12:55:17 2016

@author: Joachim
"""
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()

def create_safefile():
    #c.execute('CREATE TABLE safefile (`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, `genre`	TEXT, `prozent`	INTEGER)')
    c.execute("select prozent from g")
    data = c.fetchall()
    print(data[0])
    #c.execute("INSERT INTO safefile (rock, pop, hiphop, metal, dnb) VALUES(?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4]))
    #c.execute("INSERT INTO safefile (metal, dnb) VALUES(?, ?)", (data[0], 2))
    conn.commit()
create_safefile()
c.close()
conn.close()