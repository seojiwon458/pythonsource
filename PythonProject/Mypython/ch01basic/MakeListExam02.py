coffes = [] #empty list
coffees = list()

coffees.append('아메리카노') # 원소 추가할 때 .append = 제일 뒤에 집어 넣어라 0번
coffees.append('콜드브루') #1번
coffees.append('카푸치노') #2번
coffees.append('바닐라라떼') #3번
coffees.append('디카페인커피') #4번
coffees.append('카페라떼') #5번

count = len(coffees)
print('요소 개수 : %d' %count)

#인덱싱 : 특정한 숫자를 뽑아오는걸
print('앞에서 2번째 음료: %s' %coffees[2])
#-를 붙이면 뒤에서 부터 뽑아온다
print('앞에서 1번째 음료: %s' %coffees[-2])

#슬라이싱 : 전체데이터에서 일부분을 뽑아와서 가져오는 것
print('음료전체 출력: %s' %coffees[::]) #전부다 가져온다
print('1번째부터 3번째 음료: %s' %coffees[1:4])  #1부터 4전까지 가져온다
print('3번째이후 모든 음료: %s' %coffees[3:]) #3부터 끝까지 가져온다
print('맨앞부터 2번째까지 음료: %s' %coffees[:3]) #시작은 0이고 끝은 3까지 가져온다

print('#오름차순 정렬하기')
coffees.sort()
print(coffees)

print('#내림차순 정렬하기')
coffees.sort(reverse=True)
print(coffees)

print('#랜덤으로 섞어서 보여주기')
import random
random.shuffle(coffees)
print(coffees)
