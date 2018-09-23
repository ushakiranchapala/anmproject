from easysnmp import Session
import  sqlite3
import time
# Create an SNMP session to be used for all our requests
ip='192.168.184.23'
vl = "DEFAULT_VLAN"
session = Session(hostname=ip, community='public', version=2)
while True:
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
        #print ip,mac, port
        dbase.execute(''' INSERT INTO finalproject(IPADDRESS,VLAN,PORT,MACS) VALUES(?,?,?,?)''', (ip,vl,port,mac))

        dbase.commit()
        dbase.close
 #vlan config

 # Create an SNMP session to be used for all our requests

 
 vlansnum = []
 vlanname = []
 session = Session(hostname=ip, community='public', version=2)
 # Perform an SNMP walk
 vlans  = session.walk('.1.3.6.1.2.1.17.7.1.4.3.1.4')
 vlanindex=session.walk('.1.3.6.1.2.1.17.7.1.4.3.1.1')
 values=[]
 oids=[]
 for index,vlan in  zip(vlanindex,vlans):
    value= ':'.join('{:02x}'.format(ord(x)) for x in vlan.value)
    values=value.split(":")
    oid=vlan.oid
    oids.append(oid)
    vname=index.value
    #print values,oid,vname
    combine = ''
    if vname != "DEFAULT_VLAN":
        for i in range(len(values)):
            myhexlist = values
            myhex = myhexlist[i]
            scale = 16
            numofbits=8
            orghex = bin(int(myhex, scale))[2:].zfill(numofbits)
            #print orghex
            
            combine = combine + str(orghex)    
            orghex = ''
            #print combine
 
            listvls = list(combine)
           
           
           
        for i in range(len(listvls)):
            if listvls[i] == '1':
                #print  i
                num = i +1    
                vlanname.append(str(vname))    
                vlansnum.append(num)
                    
                
 print vlansnum
 print vlanname
 for i in range(len(vlansnum)):
     portlan = "1"
     dbase.execute(""" UPDATE finalproject SET VLAN = ?  where PORT = ? """, (vlanname[i],vlansnum[i]))
     dbase.commit()
time.sleep(60)
