#for idx in range(1,5):
#과거의 리스트를 돼대로 새로운 리스트를 만듬
mylist01 = [idx for idx in range(1,5)]
print(type(mylist01))
print(mylist01)

mylist02 = [10*idx for idx in range(1,6)]
print(mylist02)

mylist03 = [idx for idx in range(1,101,3)]
print(mylist03)

mylist04 = [idx for idx in range(1,101,3) if idx%10==0]
print(mylist04)

somedata = [75,30,85,50]
mylist05 =[jumsu for jumsu in somedata if jumsu>=60 ]
print(mylist05)

#중접for
mylist06 = [x*y for x in range(2,10) for y in range(1,10)]
print(mylist06)

fruits =[('바나나',10),('사과',20),('오렌지',30)]
for item in fruits:
    # [0]은 0번째 인덱스
    # [1]은 1번째 인덱스
    print(item[0])
    print(item[1])

mydict01 = {item[0]:item[1] for item in fruits} #사전{}
print(mydict01)

students = [('이문식',80,90,50),('강수현',50,60,80),('윤정혁',70,40,60)]
mtdict02 = {human[0]:human[1:] for human in students}
print(mtdict02)

#sum은 파이썬내장 함수
mtdict02 = {human[0]:sum(human[1:]) for human in students}
print(mtdict02)