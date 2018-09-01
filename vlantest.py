combine=''
myhexlist = ['20', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00']
for i in range(len(myhexlist)):
     myhex = myhexlist[i]
     scale = 16
     numofbits=8
     orghex = bin(int(myhex, scale))[2:].zfill(numofbits)
     print orghex
     
     combine = combine + str(orghex)
     print combine
     listvls = list(combine)
count = 1
for i in range(len(listvls)):
    if listvls[i] == '1':
    
        print  count
    count += 1
