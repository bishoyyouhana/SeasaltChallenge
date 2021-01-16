
import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import os
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split

dataFile = open("modifNumber.txt","r")
labelFile = open("train_transcripts_final.txt","r")
labels = labelFile.readlines()  
lines = dataFile.readlines()
data=[]
correct = 0
total=0
count=0

# converting data into int 
for line in lines:
    theLine = line.split(" ")
    for i in range(0, len(theLine)-1): 
        if i != "\n":
            theLine[i] = int(theLine[i])
    data.append([theLine,int(labels[count].strip())])
    count+=1
    
#split for data
train = data[0:399]
test =  data[400:]

#loading data
trainset = torch.utils.data.DataLoader(train, batch_size=10,  shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)

#Neural Network
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(190, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 100)
        self.fc4 = nn.Linear(100, 53)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

net = Net()

loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

for epoch in range(3): # Number of epochs
    for x,y in enumerate(trainset):
        print(x)
        print(y)
        net.zero_grad() 
        x= torch.FloatTensor(x[0:190])
        x= x.type(torch.FloatTensor)
        output = net(x.view(-1,190))    
        # y= int(y[0])
        # y = torch.tensor(y).unsqueeze(-1)
        loss = F.nll_loss(output,y)
        loss.backward()  
        optimizer.step()  
    print(loss)
    
correct = 0
total = 0

#Actual prediction
with torch.no_grad():
    for x, y in testset:
        output = net(x.view(-1,784))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print("Accuracy: ", round(correct/total, 3))