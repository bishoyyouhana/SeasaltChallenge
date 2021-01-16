import os

#This program formats the data so that all of them will have 190 features.

endpoints = open("train_endpoints.txt","r")
file = open("fenemeNumber.txt","r")
writeFile = open("modifNumber.txt","a")

numberfile = file.readlines()
allPoints = endpoints.readlines()
max=190 #we know this
charCount =0 
count=0
alldiffPoints = []
allNumbers = []
differences=[]
zerosAdd=0
zerosRemove=0

#converting the endpoint file to integers 
for i in allPoints:
    points = i.split("   ")
    point1 = int(points[1].strip())
    point2 = int(points[2].strip())
    alldiffPoints.append([point1,point2])
    differences.append(point2-point1)

for line in numberfile:
    point1 = alldiffPoints[count][0]
    point2 = alldiffPoints[count][1]
    print(point1, " ", point2)

    numbers = line.split(" ")
    charCount=0
    
    #Zero out the unnecessary values
    while charCount< point1:
        numbers[charCount] = "0"
        charCount+=1
    charCount = point2+1
    
    while charCount<len(numbers):
        numbers[charCount] = ""     
        charCount+=1
    count+=1
    
    zerosAdd=0
    zerosRemove=0

    #add zeros to the front and remove zeros from the end to reach a total of 190
    if point2<max:
        zerosAdd = max-point2
    else:
        zerosRemove = point2-max
        
    charCount =0
    
    while charCount< zerosAdd:
        numbers.insert(0,"0")
        charCount+=1
        
    while charCount< zerosRemove:
        numbers.pop(0)
        charCount+=1
            
    for j in numbers:
        writeFile.write(j)
        if j == "":
            writeFile.write("")
        else:
            writeFile.write(" ")
    writeFile.write("\n")
    allNumbers.append(numbers)

#print and find max
for i in differences:
    if max<i:
        max =i
print("\n max:", max)
#from this code, we see that the maximum difference between the start and end is 190.

