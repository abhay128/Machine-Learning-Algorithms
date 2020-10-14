import sys
import random
import math


eta=0.001
theta=0.001
#function for dot product
def dotproduct(w,x , cols):
    dotp=0
    refw=w
    refx=x
    for j in range(0, cols, 1):
        dotp += refw[j]*refx[j]
    return dotp

#reading data from file
datafeatures= sys.argv[1]
f = open(datafeatures)
data1 = []
i = 0
list = f.readline()
#we have updated the data file
while(list != ''): #iterate till end of the file
    a1 = list.split() #we are splitiing the file in terms of columns as a 2 different features 
    alength=len(a1)
    list2 = [] #new list is been created in which we can append the data
    for j in range(0, alength, 1):
        list2.append(float(a1[j]))
        if j ==(alength-1):
            list2.append(float(1))
    data1.append(list2)
    list = f.readline()
    
#length of rows and columns are calculated
rows = len(data1)
cols = len(data1[0])
f.close()

outputfile = sys.argv[2]

f = open(outputfile)
#trainlabels declared initialized as dictionary



#trainlabels declared initialized as dictionary
train_labels = {}
n1 = []
n1.append(0)
n1.append(0)
l = f.readline()

#swapping the key position of trainlabels
while (l != ''):
    a1 = l.split()
    train_labels[int(a1[1])] = int(a1[0])
    l = f.readline()
    n1[int(a1[0])] +=1

#intitilizing random weights, counter, terminating conditions , learning rate and error
    
weight = [0]*cols

cond=0
counter=0
diff=1
loss=rows*10

for j in range(0, cols, 1):
    weight[j] = (random.uniform(-0.01,0.01))
    


while((diff)>theta):
    delfunc=[0]*cols
    for i in range(0,rows,1):
        if train_labels.get((i))!=None:
            dot=dotproduct(weight,data1[i],cols)
            expo = (train_labels.get((i))) - (1 / (1 + (math.exp(-1 * dot))))
            for j in range(0,cols,1):
                    delfunc[j]+=(expo)*data1[i][j]
             
            
        
#updating the weights
    for j in range(0, cols, 1):
        weight[j] = weight[j] + eta*delfunc[j]
    prev=loss
    loss=0
#compute error new
    for i in range(0,rows,1):
        if (train_labels.get(i) != None):
            condition=-dotproduct(weight,data1[i],cols)
            loss-=train_labels.get(i)*(math.log(1/(1+math.e**(condition))))+(1-train_labels.get(i))*(math.log((math.e**(condition))/(1+math.e**(condition))))
    diff= abs(prev-loss)
    #print("loss=",loss)
            

print("w = ",weight)

# distane from origin
sum2=0
for j in range(0,cols-1,1):
    sum2 +=weight[j] ** 2
#print("w",weight)

#calculating the square root 
sum2=math.sqrt(sum2)


#distance from origin
#print("W:",sum2)
distance=(weight[len(weight)-1]/sum2)
#print("sum2",sum2)
#print("distance from origin:",distance)

#predictions

for i in range(0, rows, 1):
	if (train_labels.get(i) == None):
		dotpro = dotproduct(weight, data1[i], cols)
		if(dotpro>0):
			print("1",i)
		else:
			print("0",i)   
            
