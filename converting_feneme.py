#This program converts fenemes into their corresponding index at feneme_set. This allows all the fenemes to be in terms
# of numbers
import os

dataFile = open(r"train_features.txt","r")
fenemeSetFile = open(r"feneme_set.txt","r")
writeFile = open("fenemeNumber.txt","a")

feneme_set = fenemeSetFile.readlines()

returnLine =""
listLines= []

for line in dataFile:
    fenemes = line.split(" ")
    
    for feneme in fenemes:
        fenemeSetCount=0
        for i in feneme_set:    #loop to find out index number
            if feneme.strip() == i.strip():
                returnLine += str(fenemeSetCount)
                returnLine +=" "
            fenemeSetCount +=1
    
    print(returnLine)
    writeFile.write(returnLine)
    writeFile.write("\n")
    listLines.append(returnLine)
    returnLine =""