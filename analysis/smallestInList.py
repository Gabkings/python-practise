
from random import randrange
import time
def findMind(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
            if issmallest:
                overallmin = i
    return overallmin


def findMind(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar
print(findMind([5,2,3,4,7,8]))
for listSize in range(1000,10001,1000):
    alist = [randrange(1000000) for x in range(listSize)]
    start = time.time()
    print(findMind(alist))
    end = time.time()
    print("size: %d time %f" %(listSize,end-start))

#print(findMind([5,2,3,4,7,8]))