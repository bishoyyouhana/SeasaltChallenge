import os

#isolating the 53 labels to be used in convert_labels.py

labelsFile = open(r"labels.txt","a")
dataFile = open(r"train_transcripts.txt","r")
line =""
labels= []

for line in dataFile:
    if line not in labels:
        labels.append(line)
    

for i in labels:
    print(i)
    labelsFile.write(i)
    #labelsFile.write("\n")

labelsFile.close()
dataFile.close()

# this code was used to count the number of existing labels
# after running this code, we now know there are 53 labels.

