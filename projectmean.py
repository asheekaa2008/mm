import csv
with open('height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n=fileData[i][2]
    newData.append(float(n))
length=len(newData)
total=0
for x in newData:
    total=total+x
mean=total/length
print(mean)