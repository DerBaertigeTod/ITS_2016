# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 21:19:10 2016

@author: Joachim
"""

from untitled1 import farbe, dislike
from check0bis100 import check
import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()

datas = check()
dataadd=sum(datas)
welche_farbe=str(farbe)

def dislikeadd():
    print datas
    print dataadd
    print dislike
    
    if dislike==1:
        c.execute('UPDATE farbe SET rock= rock -? WHERE id=?',(dataadd, welche_farbe))
        c.execute('UPDATE farbe SET pop= pop +? WHERE id=?',(datas[1], welche_farbe))
        c.execute('UPDATE farbe SET hiphop= hiphop +? WHERE id=?',(datas[2], welche_farbe))
        c.execute('UPDATE farbe SET metal= metal +? WHERE id=?',(datas[3], welche_farbe))
        c.execute('UPDATE farbe SET reggae= reggae +? WHERE id=?',(datas[4], welche_farbe))
    else:
        if dislike==2:
            c.execute('UPDATE farbe SET rock= rock +? WHERE id=?',(datas[0], welche_farbe))
            c.execute('UPDATE farbe SET pop= pop -? WHERE id=?',(dataadd, welche_farbe))
            c.execute('UPDATE farbe SET hiphop= hiphop +? WHERE id=?',(datas[2], welche_farbe))
            c.execute('UPDATE farbe SET metal= metal +? WHERE id=?',(datas[3], welche_farbe))
            c.execute('UPDATE farbe SET reggae= reggae +? WHERE id=?',(datas[4], welche_farbe))
        else:
            if dislike==3:
                c.execute('UPDATE farbe SET rock= rock +? WHERE id=?',(datas[0], welche_farbe))
                c.execute('UPDATE farbe SET pop= pop +? WHERE id=?',(datas[1], welche_farbe))
                c.execute('UPDATE farbe SET hiphop= hiphop -? WHERE id=?',(dataadd, welche_farbe))
                c.execute('UPDATE farbe SET metal= metal +? WHERE id=?',(datas[3], welche_farbe))
                c.execute('UPDATE farbe SET reggae= reggae +? WHERE id=?',(datas[4], welche_farbe))
            else:
                if dislike==4:
                    c.execute('UPDATE farbe SET rock= rock +? WHERE id=?',(datas[0], welche_farbe))
                    c.execute('UPDATE farbe SET pop= pop +? WHERE id=?',(datas[1], welche_farbe))
                    c.execute('UPDATE farbe SET hiphop= hiphop +? WHERE id=?',(datas[2], welche_farbe))
                    c.execute('UPDATE farbe SET metal= metal -? WHERE id=?',(dataadd, welche_farbe))
                    c.execute('UPDATE farbe SET reggae= reggae +? WHERE id=?',(datas[4], welche_farbe))
                else:
                    c.execute('UPDATE farbe SET rock= rock +? WHERE id=?',(datas[0], welche_farbe))
                    c.execute('UPDATE farbe SET pop= pop +? WHERE id=?',(datas[1], welche_farbe))
                    c.execute('UPDATE farbe SET hiphop= hiphop +? WHERE id=?',(datas[2], welche_farbe))
                    c.execute('UPDATE farbe SET metal= metal +? WHERE id=?',(datas[3], welche_farbe))
                    c.execute('UPDATE farbe SET reggae= reggae -? WHERE id=?',(dataadd, welche_farbe))
                    
                
    conn.commit()
dislikeadd()
c.close()
conn.close()