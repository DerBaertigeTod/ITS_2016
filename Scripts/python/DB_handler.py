# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:15:04 2016

@author: Joachim
"""

import conf
import random
import sqlite3
conn = sqlite3.connect (DB_PATH)
c = conn.cursor()
color=3
target=4
updown=True
def get_data_by_color(farbe):
    data =[]
    c.execute("select rock from farbe WHERE id="+str(farbe)+"")
    data.append(c.fetchone()[0])
    print(data[0], 'rock')
        
    c.execute("select pop from farbe WHERE id="+str(farbe)+"")
    data.append(c.fetchone()[0])
    print(data[1], 'pop')
        
    c.execute("select hiphop from farbe WHERE id="+str(farbe)+"")
    data.append(c.fetchone()[0])
    print(data[2], 'hiphop')
    
    c.execute("select metal from farbe WHERE id="+str(farbe)+"")
    data.append(c.fetchone()[0])
    print(data[3], 'metal')
    c.execute("select reggae from farbe WHERE id="+str(farbe)+"")
    data.append(c.fetchone()[0])
    print(data[4], 'reggae')
    print ' '
    return data 

def set_data_by_color(farbe,data):
    c.execute("UPDATE farbe \
               SET rock="+str(data[0])+",pop="+str(data[1])+",hiphop="+str(data[2])+",metal="+str(data[3])+",reggae="+str(data[4])+"\
               where id = "+str(farbe)+"")
    conn.commit()

def update(color,target,up):
    datas = get_data_by_color(color)
    val2 = 0
    
    if datas[target] != 100 and datas[target] != 0:
        for key, val in enumerate(datas):
            
            if key != target and val >0 and val <100:
                if up:
                    datas[key]=val -1
                    val2 = val2 +1
                else:
                    datas[key]=val +1
                    val2 = val2 -1
            if key != target and val ==0 and not up:
                datas[key]=val +1
                val2 = val2 -1
            if key != target and val ==100 and up:
                datas[key]=val -1
                val2 = val2 +1
            
        datas[target] = datas[target] + val2
        #print datas
    set_data_by_color(color,datas)


update(color,target,updown)

def random_genre(color): 
    farbe=color
    c.execute("SELECT rock FROM farbe WHERE id="+str(farbe)+"")
    data1 = c.fetchone()[0]
    print(data1, 'rocko')
    c.execute("SELECT pop FROM farbe WHERE id="+str(farbe)+"")
    data2 = data1 + c.fetchone()[0]
    print(data2, 'pop')
    c.execute("SELECT hiphop FROM farbe WHERE id="+str(farbe)+"")
    data3 = data2 + c.fetchone()[0]
    print(data3, 'hiphop')
    c.execute("SELECT metal FROM farbe WHERE id="+str(farbe)+"")
    data4 = data3 + c.fetchone()[0]
    print(data4, 'metal')
    c.execute("SELECT reggae FROM farbe WHERE id="+str(farbe)+"")
    data5 = data4 + c.fetchone()[0]
    print(data5, 'reggae')
    
    randnumb=random.randrange(1,100)
    #print(randnumb)
    if data1>=randnumb:
        print('play rock')
        genre='rock'
    else:
        if data2>=randnumb:
            print('play pop')
            genre='pop'
        else:
            if data3>=randnumb:
                print('play hiphop')
                genre='hiphop'
            else:
                if data4>=randnumb:
                    print('play metal')
                    genre='metal'
                else:
                    print('play reggae')
                    genre='reggae'
    return genre



def random_track(): 
    genre = random_genre(color)
    c.execute('SELECT MAX(id) FROM '+genre)
    maxid = c.fetchone()[0]
    randnumb=random.randrange(1, maxid)    
    c.execute('SELECT trackname FROM '+genre+' WHERE id= '+str(randnumb))
    trackname=c.fetchone()
    print trackname[0]
    c.execute('SELECT dateipfad FROM '+genre+' WHERE id= '+str(randnumb))
    dateipfad=c.fetchone()
    print dateipfad[0]
    c.execute('SELECT interpret FROM '+genre+' WHERE id= '+str(randnumb))
    interpret=c.fetchone()
    print interpret[0]
    return([trackname, dateipfad])
    c.close()
    conn.close()
    
random_track()

 