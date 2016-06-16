# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:06:16 2016

@author: Joachim
"""
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
farbe='1'
like=1


def check():
    
    c.execute("select rock from farbe WHERE id=?", farbe)
    data =c.fetchone()[0]
    #print(data, 'rock')
    #if data<=0 or data>=100:
    if like!=1 and data in range(1,99):
        data1=1
    else:
        data1=0
    #print(data1, 'antwort')
        
        
        
    c.execute("select pop from farbe WHERE id=?", farbe)
    data =c.fetchone()[0]
    #print(data, 'pop')
    if like!=2 and data in range(1,99):
        data2=1
    else:
        data2=0
    #print(data2, 'antwort')
        
    c.execute("select hiphop from farbe WHERE id=?", farbe)
    data =c.fetchone()[0]
    #print(data, 'hiphop')
    if like!=3 and data in range(1,99):
        data3=1
    else:
        data3=0
    
    c.execute("select metal from farbe WHERE id=?", farbe)
    data =c.fetchone()[0]
    #print(data, 'metal')
    if like!=4 and data in range(1,99):
        data4=1
    else:
        data4=0
    
    c.execute("select dnb from farbe WHERE id=?", farbe)
    data =c.fetchone()[0]
    #print(data, 'dnb')
    if like!=5 and data in range(1,99):
        data5=1
    else:
        data5=0
    
    dataadd=data1+data2+data3+data4+data5
    print(dataadd, 'Summe')

    
 
check()
