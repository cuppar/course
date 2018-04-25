import re
regex=re.compile("[,\\n]")
csvFile=open('学生信息表.csv', 'r')
headerLine=regex.split(csvFile.readline())
headerLine.pop()
jsons=[]
for line in csvFile:
    messageList=regex.split(line)
    tempDict={}
    count=0
    for key in headerLine:
        tempDict[key]=messageList[count]
        count+=1
    jsons.append(tempDict)
print(jsons)