#이름을
print('이름 입력 :', end = '') # end ='' : 출력한 후 줄바꿈을 하지 않고 다음 출력을 같은 줄에 이어서 하도록 하는 구문
#input 함수는 반환 타입이 문자열입니다 숫자로 바꾸려면 형변환
name = input()
age =  int(input('나이 입력 :'))
height = float(input('키 입력 :')) # 실수는 무조건 float

print('%포맷 코드로 출력')
print('이름 : %s' %name) #name이 %S로 출력
print('나이 : %d' %age) #age는 %d로 출력
print('키 : %2f' %height) #height는 %2f로 출력

message = (f'제 이름은 {name}이고, 나이는 {age}세 입니다. \n제 키는 {height}cm 입니다.')
print(message.format(name,age,height)) #0번째 name, 1번째 나이, 2번째 키