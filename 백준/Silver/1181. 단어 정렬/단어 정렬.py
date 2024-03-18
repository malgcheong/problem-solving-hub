MAX_TEXT_LENGTH = 51

textLengthList = [0] * 51
inputList = []
answerList = []

for _ in range(int(input())):

    text = input()
    length = len(text)
    inputList.append(text)
    textLengthList[length] += 1

inputList.sort()

for i in range(1, len(textLengthList)):
    lengthCount = textLengthList[i]
    if lengthCount:
        for j in range(len(inputList)):
            if(len(inputList[j]) == i):
                if inputList[j] not in answerList:
                    answerList.append(inputList[j])
                
for li in answerList:
    print(li)

