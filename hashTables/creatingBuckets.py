a = [0,0,1,1,2,1,7,8,7,9,9]
#a = [0,0,2,5,0,5,8,9,5,6,9,11,12]

bucketDict = {}

for index,value in enumerate(a):
    if value not in bucketDict:
        bucketDict[value] = [index,index]
    else:
        bucketDict[value][1] = index

print(bucketDict)

b = []
count = 0

for i in bucketDict:
    if count == 0:
        b.append(a[bucketDict[i][0]:bucketDict[i][1] + 1])
        count += 1
    else:
        if bucketDict[i][0] < lastBound:
            if bucketDict[i][1] > lastBound:
                temp = a[lastBound + 1 : bucketDict[i][1] + 1]
                b[-1] = b[-1] + temp
        else:
            b.append(a[bucketDict[i][0]:bucketDict[i][1] + 1])
    lastBound = bucketDict[i][1]

print(b)
                
        
