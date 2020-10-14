import sys
datafile = sys.argv[1]
labelfile = sys.argv[2]


f = open(datafile)
data = []
i=0
l = f.readline()
#** Read Data **
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    #l2.append(1)
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()
#print(rows,cols)
#print (data)


#** Read labels **

f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()

while(l != ''):
    a = l.split()
    if(int(a[0]) == 0):
        trainlabels[int(a[1])] = -1
    else:
        trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1

#print (trainlabels)

def classify(data,trainlabels):
    trainD = []
    testD = []
    trainL = []
    for i in range(0, rows, 1):
        if(trainlabels.get(i)!=None):
            trainD.append(data[i])
            trainL.append(trainlabels.get(i))
        else:
            testD.append(data[i])
    return (trainD,testD,trainL)

traindata, testdata, trainlbl = classify(data,trainlabels)
#print (traindata) 
#print (trainlbl)


def gini_split(traindata, trainlbl):
    rows = len(traindata)
    col_data = []
    train_label = []
    
    for j in range(0,cols,1):
        val = []
        label = []
        for i in range(0,rows,1):
            #if(trainlabels.get(i)!= None):
            val.append(traindata[i][j])
            label.append(trainlbl[i])
        train_label.append(label)
        col_data.append(val)
        
    #print (col_data)
    #print (train_label)
    
    gini_val = []
    splits = []
    for j in range(0,cols,1):
        for i in range(0,rows,1):
            split_val = col_data[j][i]
            left_val = []
            right_val = []
            for k, val in enumerate(col_data[j]):
                if val < split_val:
                    left_val.append(train_label[j][k])
                else:
                    right_val.append(train_label[j][k])
            #print(left_val)
            #print(right_val)
    
            lsize = len(left_val)
            rsize = len(right_val)
    
            #print (rsize)
    
            lp = sum([1 if lab == -1 else 0 for lab in left_val])
            rp = sum([1 if lab == -1 else 0 for lab in right_val])
    
            if lsize == 0:
                left = 0
            else:
                left = (lsize/rows) * (lp/lsize) * (1-(lp/lsize))
    
            if rsize == 0:
                right = 0
            else:
                right = (rsize/rows) * (rp/rsize) * (1-(rp/rsize))
    
            gini = left + right
            gini_val.append(gini)
            #print ("gini_val::",gini)
    
            left_split = []
            for val in col_data[j]:
                if val < split_val:
                    left_split.append(val)
                    
                if len(left_split) != 0:
                    left_max = max(left_split)
                else:
                    left_max = split_val
                    
            main_split = (left_max + split_val)/2
            splits.append([j,main_split])
            #print ("\nX <",col_data[j][i])
            #print ("gini:",gini)
            #print ("Split value",main_split)
        #print (gini_val)
        #print (splits)
            
    min_gini = min(gini_val)
    index_val = gini_val.index(min_gini)
   #a,b = splits[index_val]
    #print(a)
    #print(" "+ str(b))
    #print (splits[index_val])
    return (splits[index_val])

#print ()
a,b = gini_split(traindata,trainlbl)
print(a,end = " ")
print(b)
#print(gini_split(traindata,trainlbl))

