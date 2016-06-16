# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 21:19:10 2016

@author: Joachim
"""

import sqlite3
conn = sqlite3.connect('C:\Users\Joachim\Documents\GitHub\ITS_2016\Datenbank\its_datenbank.db')
c = conn.cursor()
def del_and_update():
    c.execute("select rock from safefile WHERE id=1")
    data = c.fetchone()
    c.execute('UPDATE g SET prozent= ? WHERE id=1',(data))
    
    c.execute("select pop from safefile WHERE id=1")
    data = c.fetchone()
    c.execute('UPDATE g SET prozent= ? WHERE id=2', (data))
    
    c.execute("select hiphop from safefile WHERE id=1")
    data = c.fetchone()
    c.execute('UPDATE g SET prozent= ? WHERE id=3', (data))
    
    c.execute("select metal from safefile WHERE id=1")
    data = c.fetchone()
    c.execute('UPDATE g SET prozent= ? WHERE id=4', (data))
    
    c.execute("select dnb from safefile WHERE id=1")
    data = c.fetchone()
    c.execute('UPDATE g SET prozent= ? WHERE id=5', (data))
    conn.commit()
    
del_and_update()
c.close()
conn.close()

"rock"
"pop"
"hiphop"
"metal"
"dnb"
