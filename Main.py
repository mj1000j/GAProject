from random import randrange
def f(x): #20 기준 적합도
    return abs(20-sum(x))
a=[1,5,3,8,0,9,9,8,9,3,7,5,4,3,2] #리스트
li=[] #유전자 초기 상태 +적합도
for i in range(len(a)):
    if(i%3==0):li.append([a[i]])
    else:li[-1].append(a[i])
for j in range(len(li)):
    li[j].append(f(li[j]))
c=int(input("반복 횟수를 입력하세요: ")) # 반복 횟수
for _ in range(c):
    li.sort(key=lambda x:(x[-1]))
    newli=li[:2] # 새로운 리스트
    index=randrange(0,len(li[0])-1) # 교환할 원소값 (무작위)

    newgene1=newli[0][:]
    newgene1[index]=newli[1][index]
    newgene1[-1]=f(newgene1[:-1])
    
    newgene2=newli[1][:]
    newgene2[index]=newli[0][index]
    newgene2[-1]=f(newgene2[:-1])

    newli.append(newgene1)
    newli.append(newgene2)

    li=newli
li.sort(key=lambda x:(x[-1]))
print(li[0])