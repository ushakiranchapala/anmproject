from easysnmp import Session
import  sqlite3
import time
# Create an SNMP session to be used for all our requests
ip='192.168.184.23'



vl = "DEFAULT_VLAN(1)"

while True:
 dbase = sqlite3.connect('ourdata2.db')
 data = dbase.execute("select * from manager")
 for cred in data:
  # Perform an SNMP walk
  
  ipadd = cred[0]
  portadd = cred[1]
  community = cred[2]
  version = cred[3]
  try:
   session = Session(hostname=ipadd, community=community, version=2)
   print "ip =  %s port= %s com= %s ver= %s EOL" % (ipadd, portadd, community, version) 
   macs     = session.walk('.1.3.6.1.2.1.17.4.3.1.1')
   ports = session.walk('.1.3.6.1.2.1.17.4.3.1.2')
  except:
   print "timeout"
   continue
  starttime = time.time()
  fintime=time.ctime(int(starttime))
  print "ok"
  #print system_items
  
  
  for a,b in zip(macs,ports):
     
         oid=a.oid
         oid_index=a.oid_index
         snmp_type=a.snmp_type
         mac=':'.join('{:02x}'.format(ord(x)) for x in a.value)
         portval =b.value
         
         print ip,mac, portval
         data = dbase.execute("SELECT * from finalproject where (PORT =? AND IPADDRESS=?)", (portval,ip,))
         rows = data.fetchall()
         for finalmacs in rows:
           k = finalmacs[3]
         if len(rows)==0:
           print ip,mac,portval
           dbase.execute(''' INSERT INTO finalproject(IPADDRESS,VLAN,PORT,MACS) VALUES(?,?,?,?)''', (ip,vl,portval,mac))
 
           dbase.commit()
         elif len(rows)==1 and k.find(mac) is -1:
           endmac=k+","+mac
           dbase.execute("UPDATE finalproject set MACS=? where PORT = ?",(endmac,portval,))
           dbase.commit()
         dbase.execute("UPDATE manager set firstprob=?, lastprob=? where ip = ?",(fintime,fintime,ip,))
         dbase.commit()
         
         
  #vlan config

  # Create an SNMP session to be used for all our requests

 
  vlansnum = []
  vlanname = []
  
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
    # print oids
     vnums = oid.split('.')
     vnum =str(vnums[-1])
     
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
                 vlanname.append(str(vname)+"("+vnum+")")    
                 vlansnum.append(num)
                    
                
  print vlansnum
  print vlanname
  for i in range(len(vlansnum)):
      portlan = "1"
      dbase.execute(""" UPDATE finalproject SET VLAN = ?  where PORT = ? """, (vlanname[i],vlansnum[i]))
      dbase.commit()
 dbase.close
 time.sleep(60)
