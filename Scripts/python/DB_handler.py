# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:15:04 2016

@author: Joachim
"""
import conf
import random
import sqlite3
import math
conn = sqlite3.connect (DB_PATH)
c = conn.cursor()

#"farben"
#red= channel_buffer[2]
#green= channel_buffer[3]
#blue= channel_buffer[4]
#
#"Genre das einen Like/dislike bekommt"
#target=4
#"like, dislike"
#updown=True



"bestimmt die farbe"
def get_color_name(r,g,b):
    deltas = {}
    smallest = 999999999999999999
    smalest_name = ''
    #colors ={'red':[255,0,0],'orange':[255,165,0],'yellow':[255,255,0],'green':[0,255,0],'blue':[0,0,255],'violett':[238,130,238]}
    colors ={'1':[255,0,0],'6':[255,165,0],'5':[255,255,0],'2':[0,255,0],'3':[0,0,255],'4':[238,130,238]}
    for c_key, c_val in enumerate(colors):
        deltas[c_val] =  math.sqrt((colors[c_val][0]-r)*(colors[c_val][0]-r)+(colors[c_val][1]-g)*(colors[c_val][1]-g)+(colors[c_val][2]-b)*(colors[c_val][2]-b))
        
    for key, val in enumerate(colors):
          if deltas[val] < smallest:
              smallest = deltas[val]
              smallest_name = val

    
    return smallest_name
    
color= get_color_name(red,green,blue)

"liest die alten Werte aus"
def del_and_update():
    c.execute('UPDATE color SET rock= 20')
    c.execute('UPDATE color SET pop= 20')
    c.execute('UPDATE color SET hiphop= 20')
    c.execute('UPDATE color SET metal= 20')
    c.execute('UPDATE color SET reggae= 20')
    conn.commit()

def pfad():
    c.execute("UPDATE hiphop SET dateipfad= ('C:\Users\Joachim\Desktop\music\hiphop')")
    conn.commit()


def get_data_by_color(color):
    data =[]
    c.execute("select rock from color WHERE id="+str(color)+"")
    data.append(c.fetchone()[0])
#    print(data[0], 'rock')
        
    c.execute("select pop from color WHERE id="+str(color)+"")
    data.append(c.fetchone()[0])
#    print(data[1], 'pop')
        
    c.execute("select hiphop from color WHERE id="+str(color)+"")
    data.append(c.fetchone()[0])
#    print(data[2], 'hiphop')
    
    c.execute("select metal from color WHERE id="+str(color)+"")
    data.append(c.fetchone()[0])
#    print(data[3], 'metal')
    c.execute("select reggae from color WHERE id="+str(color)+"")
    data.append(c.fetchone()[0])
#    print(data[4], 'reggae')
#    print ' '
    return data 

"updatet die Werte"
def set_data_by_color(color,data):
    c.execute("UPDATE color \
               SET rock="+str(data[0])+",pop="+str(data[1])+",hiphop="+str(data[2])+",metal="+str(data[3])+",reggae="+str(data[4])+"\
               where id = "+str(color)+"")
    conn.commit()

"legt die Updatewerte fest"
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


#update(color,target,updown)

#"bestimmt das Genre"
def random_genre(color):
    c.execute("SELECT rock FROM color WHERE id="+str(color)+"")
    data1 = c.fetchone()[0]
#    print(data1, 'rocko')
    c.execute("SELECT pop FROM color WHERE id="+str(color)+"")
    data2 = data1 + c.fetchone()[0]
#    print(data2, 'pop')
    c.execute("SELECT hiphop FROM color WHERE id="+str(color)+"")
    data3 = data2 + c.fetchone()[0]
#    print(data3, 'hiphop')
    c.execute("SELECT metal FROM color WHERE id="+str(color)+"")
    data4 = data3 + c.fetchone()[0]
#    print(data4, 'metal')
    c.execute("SELECT reggae FROM color WHERE id="+str(color)+"")
    data5 = data4 + c.fetchone()[0]
#    print(data5, 'reggae')
    
    randnumb=random.randrange(1,100)
    #print(randnumb)
    if data1>=randnumb:
#        print('play rock')
        genre='rock'
    else:
        if data2>=randnumb:
 #           print('play pop')
            genre='pop'
        else:
            if data3>=randnumb:
#                print('play hiphop')
                genre='hiphop'
            else:
                if data4>=randnumb:
#                    print('play metal')
                    genre='metal'
                else:
#                    print('play reggae')
                    genre='reggae'
    return genre


"wählt einen zufälligen Track aus Genre"
def random_track(color): 
    genre = random_genre(color)
    c.execute('SELECT MAX(id) FROM '+genre)
    maxid = c.fetchone()[0]
    randnumb=random.randrange(1, maxid)    
    c.execute('SELECT trackname FROM '+genre+' WHERE id= '+str(randnumb))
    trackname=c.fetchone()
#    print trackname[0]
    c.execute('SELECT dateipfad FROM '+genre+' WHERE id= '+str(randnumb))
    dateipfad=c.fetchone()
#    print dateipfad[0]
    c.execute('SELECT interpret FROM '+genre+' WHERE id= '+str(randnumb))
    interpret=c.fetchone()
#    print interpret[0]
    return(trackname, dateipfad, interpret)
    c.close()
    conn.close()
    
#random_track()
