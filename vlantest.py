myhex = "50"
scale = 16
numofbits=8
orghex = bin(int(myhex, scale))[2:].zfill(numofbits)
print orghex
count = 1
combine = str(orghex) + '0010000'
print combine
listvls = list(combine)
for i in range(len(listvls)):
    if listvls[i] == '1':
    
        print  count
    count += 1
