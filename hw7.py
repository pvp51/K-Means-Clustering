import sys
from sys import argv
import math
import copy
import sys

################
##  py hw7.py datafile numberOfCluster
################

#####
## Calculate distance
######
def calcDist(d, index, m):
    minValue = sys.maxsize
    for i in  range (0, numK):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(d, m[i])]))
        if(distance < minValue):
            minValue = distance
            trainlabels[index] = i
        print("Distance: ",distance)

################
##Read Data
################
f = open(argv[1])
data = []
l = f.readline()
while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
dataRows = len(data)
dataCols = len(data[0])
f.close()

################
##Read Number of Clusters
###############
numK = int(sys.argv[2])

################
##Main
###############

##Initializing clusters
trainlabels={}
k = 0
for j in range(0, dataRows, 1): 
    if(k < numK):
        trainlabels[j] = k
        k+=1
    else:
        k = 0
        trainlabels[j] = k
        k+=1

##Initialize mean
m0=[]
for j in range(0,dataCols,1):
    m0.append(0)
m=[]
for i in range(0,numK,1):
    x = copy.deepcopy(m0)
    m.append(x)

#print("Initial Mean : ",m)
print("Before Trainlabels : ",trainlabels)
##Calculate mean
n = [0] * numK;
for i in range(0, numK, 1):
    for x in range(0, dataRows, 1):
        if(trainlabels.get(x) == i):
            n[i] = n[i] + 1;
            for j in range(0,dataCols,1):
                #print("Cluster: ",i ,"Row: ",x," col : ",j);
                #print("Value :", data[x][j]);
                m[i][j] += data[x][j]
    #print("N: ",n)

for i in range(0,numK,1):
    for j in range(0,dataCols,1):
        m[i][j] /= n[i];

for i in range(0, dataRows):
    calcDist(data[i], i, m)




################
##Classify unlabeled points
###############
#for i in range(0, dataRows, 1):
print("Data : ",data)
print("Mean : ",m)
print("After trainlabels : ",trainlabels)

