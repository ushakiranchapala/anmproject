from easysnmp import Session
import  sqlite3

# Create an SNMP session to be used for all our requests
ip='192.168.184.23'
vl = 20
session = Session(hostname=ip, community='public', version=2)
# Perform an SNMP walk
macs     = session.walk('.1.3.6.1.2.1.17.4.3.1.1')
ports = session.walk('.1.3.6.1.2.1.17.4.3.1.2')

#print system_items
dbase = sqlite3.connect('ourdata2.db')
dbase.execute(''' CREATE TABLE IF NOT EXISTS finalproject(

            IPADDRESS TEXT NOT NULL,
            VLAN TEXT NOT NULL,
            PORT TEXT NOT NULL,
            MACS TEXT NOT NULL)''')
for a,b in zip(macs,ports):
    
        oid=a.oid
        oid_index=a.oid_index
        snmp_type=a.snmp_type
        mac=':'.join('{:02x}'.format(ord(x)) for x in a.value)
        port=b.value
        print ip,mac, port
        dbase.execute(''' INSERT INTO finalproject(IPADDRESS,VLAN,PORT,MACS) VALUES(?,?,?,?)''', (ip,vl,port,mac))

        dbase.commit()
        dbase.close




