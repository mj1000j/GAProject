from random import randrange

def f(x):
    return abs(5000-sum(x))
def solve(c,li):
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

        #돌연변이
        rand=randrange(1,30)
        if(rand==1):
            newgene1[index]=li[randrange(0,len(li))]

        li=newli
    li.sort(key=lambda x:(x[-1]))
    return li

#리스트
a=[1199, 1737, 1129, 1089, 1549, 1535, 1185, 1816, 1350, 1714, 1816, 1714, 1173, 1643, 1610]
#유전자 초기 상태 +적합도
li=[]
for i in range(len(a)):
    if(i%3==0):li.append([a[i]])
    else:li[-1].append(a[i])
for j in range(len(li)):
    li[j].append(f(li[j]))
c=int(input("반복 횟수를 입력하세요: ")) # 반복 횟수
print(solve(c,li)[0])