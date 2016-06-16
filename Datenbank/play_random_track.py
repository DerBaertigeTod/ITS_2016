# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 13:32:53 2016

@author: Joachim
"""

import random
import play_random_genre

import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()

genre = random_genre()
print genre

def random_track(): 
    c.execute('SELECT MAX(id) FROM ?', genre)
    maxid = c.fetchone()[0]
    randnumb=random.randrange(1, maxid)    
    c.execute('SELECT trackname FROM ? WHERE id=?', (genre, str(randnumb)))
    trackname=c.fetchall()
    print trackname[0]
    c.execute('SELECT dateipfad FROM ? WHERE id=?', (genre, str(randnumb)))
    dateipfad=c.fetchall()
    print dateipfad[0]
    c.execute('SELECT interpret FROM ? WHERE id=?', (genre, str(randnumb)))
    interpret=c.fetchall()
    print interpret[0]
    return([trackname, dateipfad])
random_track()

c.close()
conn.close()