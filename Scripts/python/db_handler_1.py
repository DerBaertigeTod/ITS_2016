# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:06:16 2016

@author: Joachim
"""
"""

"""
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()

def get_data_by_color(farbe):
    c.execute("select rock from farbe WHERE id=?", farbe)
    data[0] =c.fetchone()[0]
    print(data, 'rock')
        
    c.execute("select pop from farbe WHERE id=?", farbe)
    data[1] =c.fetchone()[0]
    print(data, 'pop')
        
    c.execute("select hiphop from farbe WHERE id=?", farbe)
    data[2] =c.fetchone()[0]
    print(data, 'hiphop')
    
    c.execute("select metal from farbe WHERE id=?", farbe)
    data[3] =c.fetchone()[0]
    print(data, 'metal')
    c.execute("select reggae from farbe WHERE id=?", farbe)
    data[4] =c.fetchone()[0]
    print(data, 'reggae')
    return(data)

def set_data_by_color(farbe,data):
    c.execute("UPDATE table_name \
               SET rock=?,pop=?,hiphop=?,metal=?,raggae=?\
               where id = ?",data[0],data[1],data[2],data[3],data[4], farbe)
    
#import der Additionswerte als Variablen

#c.close()
#conn.close()    
   
