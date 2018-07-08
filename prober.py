from easysnmp import Session
import time
mac = session.walk('.1.3.6.1.2.1.17.4.3.1.1')
print mac

import sqlite3

conn = sqlite3.connect('test.db')
c= conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS table1(unix REAL, datestamp TEXT, key$

def data_entry():
    c.execute("INSERT INTO table1 VALUES(14512, '2016-01-02', 'python', 8)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()

