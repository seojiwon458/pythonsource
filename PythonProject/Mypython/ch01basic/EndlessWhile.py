import random #파이썬에서 random을 불러오는 구문

answer = random.randint(1,100);
#print('정답 : %d' %answer)

counter = 0 #카운터 변수

while True : #갯수가 명백하게 정해지지 않을 때 사용
    su = int(input('1부터 100사이의 정수1개 입력 :'))
    counter += 1
    if answer > su:
        print('%d 보다 큰 수를 입력해주세요.' %su)
    elif answer<su:
        print('%d 보다 작은 수를 입력해주세요.' %su)
    else:
        print('정답을 맞추셨군요')
        break

print('%d번만에 맞추었습니다.' %counter)