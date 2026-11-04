#管你的，标记一下
lis=[]
count=[]
seen=[]
while True:
    try:
        say=input().strip().upper()
        lis.append(say)
    except EOFError:
        break
for i in sorted(lis):
    #字典不等同于字符串，不能直接在里面找
    if i in seen:
        continue
    cout=int(0)
    for j in lis:
        if i==j:
            cout+=1
    seen.append(i)
    count.append({"cout":cout,"i":i})
for i in count:
    print(i["cout"],i["i"])

"""
from collections import Counter

lis = []
while True:
    try:
        say = input().strip().upper()
        lis.append(say)
    except EOFError:
        break

#  直接统计每个元素出现次数
cnt = Counter(lis)

#  sorted 按单词排序
for word, num in sorted(cnt.items()):
    print(num, word)
"""