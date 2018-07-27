from easysnmp import Session
import time
mac = session.walk('.1.3.6.1.2.1.17.4.3.1.1')
print mac

import sqlite3

conn = sqlite3.connect('test.db')
c= conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS table1(unix REAL, datestamp TEXT, port  TEXT, mac REAL)')

def data_entry():
    c.execute("INSERT INTO table1 VALUES(2, 12, 80 , 1)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
sleep(5)

