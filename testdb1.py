import  sqlite3
ip = '123.34.45.56'
vl ='12'
ports = '943'
mac = 'ssn5'
dbase = sqlite3.connect('ourdata1.db')

dbase.execute(''' CREATE TABLE IF NOT EXISTS finalproject(
            
            IPADDRESS TEXT NOT NULL,
            VLAN TEXT NOT NULL,
            PORT TEXT NOT NULL,
            MACS TEXT NOT NULL)''')
dbase.execute(''' INSERT INTO finalproject(IPADDRESS,VLAN,PORT,MACS) VALUES(?,?,?,?)''', (ip,vl,ports,mac))

dbase.commit()
dbase.close
