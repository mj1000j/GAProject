from bisect import bisect
from random import randrange

def roulette(li):
    sumli=[0]
    maxli=max([i[-1] for i in li])
    for i in li:
        sumli.append(sumli[-1]+i[-1])
    x1=bisect(sumli,randrange(1,sumli[-1]))
    x2=bisect(sumli,randrange(1,sumli[-1]))
    return [li[x1-1],li[x2-1]] 
def f(x):
    global a2
    return abs(a2-sum(x))
def solve(a,c,li):
    for _ in range(c):
        newli=roulette(li) # 새로운 리스트
        index=randrange(0,len(li[0])-2) # 교환할 원소값 (무작위)
        index2=randrange(index+1,len(li[0])-1)

        newgene1=newli[0][:]
        newgene1[index:index2]=newli[1][index:index2]
        newgene1[-1]=f(newgene1[:-1])
    
        newgene2=newli[1][:]
        newgene2[index:index2]=newli[0][index:index2]
        newgene2[-1]=f(newgene2[:-1])

        #돌연변이
        rand=randrange(1,30)
        if(rand==1):
            newgene1[randrange(0,len(newgene1))]=a[randrange(0,len(li))]
        if(rand==2):
            newgene2[randrange(0,len(newgene1))]=a[randrange(0,len(li))]

        newli.append(newgene1)
        newli.append(newgene2)
        
        li=newli
    li.sort(key=lambda x:(x[-1]))
    return li

#리스트
a=list(map(int,input().split()))
a2=int(input('목표값(수의 합)을 입력해 주세요 : '))
a3=int(input('수의 개수를 입력해 주세요 : '))
#유전자 초기 상태 + 적합도
li=[]
for i in range(len(a)):
    if(i%a3==0):li.append([a[i]])
    else:li[-1].append(a[i])
for j in range(len(li)):
    li[j].append(f(li[j]))
c=int(input("반복 횟수를 입력하세요: ")) # 반복 횟수
print(solve(a,c,li)[0])
