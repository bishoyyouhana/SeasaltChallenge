# This program converts labels from their names to their index in labels.txt (a number). to be used by pytorch
import os

labelFile = open("train_transcripts.txt","r")
writeFile = open("train_transcripts_final.txt","w")
label_setFile = open("labels.txt","r")

label_set = label_setFile.readlines()
labels = labelFile.readlines()

for label in labels:
    count=1
    for i in label_set:
        if label.strip() == i.strip():
            print(label, " ", i)
            writeFile.write(str(count))
            writeFile.write("\n")
        count+=1