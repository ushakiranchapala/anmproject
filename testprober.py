from easysnmp import Session
# Create an SNMP session to be used for all our requests
session = Session(hostname='192.168.184.23', community='public', version=2)
# Perform an SNMP walk
oid=[]
oid=['.1.3.6.1.2.1.17.4.3.1.1','.1.3.6.1.2.1.17.4.3.1.2']
system_items = session.walk(oid)
port=0
#print system_items

for item in system_items:
    
        oid=item.oid
        oid_index=item.oid_index
        snmp_type=item.snmp_type
        if snmp_type == 'OCTETSTR':
         mac=':'.join('{:02x}'.format(ord(x)) for x in item.value)
         print mac
        else:
         port=item.value
         print port

