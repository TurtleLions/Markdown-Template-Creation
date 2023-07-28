import mdcreation

fileName = str(input("What is the file name? (excluding .md)"))
print(fileName)
title = str(input("What is the title?"))
print(title)
numSections = int(input("How many sections are required?"))
print(numSections)
sectionArray = []
for i in range(numSections):
  sectionHeader = str(input("Name of section"))
  print(sectionHeader)
  sectionBody = str(input("Text of body"))
  print(sectionBody)
  sectionArray.append([sectionHeader, sectionBody])

mdcreation.creation(fileName)
mdcreation.textCreation(fileName, title, sectionArray)