# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 13:32:53 2016

@author: Joachim
"""
from untitled1 import farbe, like
import random


import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
farbauswahl=str(farbe)

def random_genre(): 
    c.execute("SELECT rock FROM farbe WHERE id=?",farbauswahl)
    data1 = c.fetchone()[0]
    #print(data1, 'rock')
    c.execute("SELECT pop FROM farbe WHERE id=?",farbauswahl)
    data2 = data1 + c.fetchone()[0]
    #print(data2, 'pop')
    c.execute("SELECT hiphop FROM farbe WHERE id=?",farbauswahl)
    data3 = data2 + c.fetchone()[0]
    #print(data3, 'hiphop')
    c.execute("SELECT metal FROM farbe WHERE id=?",farbauswahl)
    data4 = data3 + c.fetchone()[0]
    #print(data4, 'metal')
    c.execute("SELECT reggae FROM farbe WHERE id=?",farbauswahl)
    data5 = data4 + c.fetchone()[0]
    #print(data5, 'reggae')
    
    randnumb=random.randrange(1,100)
    #print(randnumb)
    if data1>=randnumb:
        #print('play rock')
        genre='rock'
    else:
        if data2>=randnumb:
        #    print('play pop')
            genre='pop'
        else:
            if data3>=randnumb:
         #       print('play hiphop')
                genre='hiphop'
            else:
                if data4>=randnumb:
          #          print('play metal')
                    genre='metal'
                else:
           #         print('play reggae')
                    genre='reggae'
    return(genre)
random_genre()
c.close()
conn.close()