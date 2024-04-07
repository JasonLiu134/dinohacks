import pandas as pd
import os

def processData(folderpath):
    fileList = os.listdir(folderpath)
    df = pd.DataFrame(columns=['type', 'lyrics'])
    for filepath in fileList:
        try:
            with open(folderpath + '/' + filepath, 'r') as f:
                lyricstring = f.read().strip()
                df.loc[len(df.index)] = [lyricstring[0], lyricstring[2:]]
        except:
            pass

def classifyString(s):
    s = s.split(' ')
    d = {}
    for word in s:
        if word not in d and s != 'dinosaur':
            d[word] = 1
        else:
            d[word] += 1    

    return d

def classifyCSV(t, csvfile):
    df = pd.read_csv(csvfile)
    totalDict = {}

    for i in range(len(list(df.get('lyrics')))):
        if df.get('type')[i] == t:
            oneDict = classifyString(df.get('lyrics')[i])
            for key in oneDict:
                if key not in totalDict:
                    totalDict[key] = oneDict[key]
                else:
                    totalDict[key] += oneDict[key]
    
    return totalDict

def testClassify(s):
    data = 'training_data.csv'
    class0 = classifyCSV(0, data)
    class1 = classifyCSV(1, data)
    class2 = classifyCSV(2, data)

    type0 = 0
    type1 = 0
    type2 = 0

    s = s.split(' ')
    for word in s:
        if word in class0.keys():
            type0 += class0[word]
        if word in class1:
            type1 += class1[word]
    if type0 > type1 and type0 > type2:
        return "Old person"
    elif type1 > type2:
        return "Dinosaur!"
    else:
        return "Other use"

def description():
    return 'Use by entering a string, and the processor will classify the context in which the word "Dinosaur" is being used (as an actual dinosaur, referring to someone/something very old, or in some other context)' 