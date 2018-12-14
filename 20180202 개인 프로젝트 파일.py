import requests
import re

r = requests.get("https://music.naver.com/lyric/index.nhn?trackId=1964907")
r.encoding='utf8'
data = r.text
data = data[data.find('Aha! Listen Boy'):data.rfind('Oh 좋은 향기 Oh Ye Ye Ye')+20]

data = re.sub('<br.+?>',' ', data)
data = data.replace('.', ' ')
data = data.replace(',', ' ')
print(data)
data = data.split()

mydict = {}
for w in data:
    if w in mydict: mydict[w] += 1
    else: mydict[w] = 1
    
print(mydict)
for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    print(k, mydict[k])

    

r = requests.get("https://music.naver.com/lyric/index.nhn?trackId=2510284")
r.encoding='utf8'
data = r.text
data = data[data.find('Hot Hot Hot Hot Summer Hot Hot Hot Hot Breath'):data.rfind('Hot Hot Hot Hot Breath')+22]

data = re.sub('<br.+?>',' ', data)
data = data.replace('.', ' ')
data = data.replace(',', ' ')
print(data)
data = data.split()

mydict = {}
for w in data:
    if w in mydict: mydict[w] += 1
    else: mydict[w] = 1
    
print(mydict)
for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    print(k, mydict[k])

    

r = requests.get("https://music.naver.com/lyric/index.nhn?trackId=21615201")
r.encoding='utf8'
data = r.text
data = data[data.find('You can call me artist'):data.rfind('얼쑤')+2]

data = re.sub('<br.+?>',' ', data)
data = data.replace('.', ' ')
data = data.replace(',', ' ')
print(data)
data = data.split()

mydict = {}
for w in data:
    if w in mydict: mydict[w] += 1
    else: mydict[w] = 1
    
print(mydict)
for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    print(k, mydict[k])
