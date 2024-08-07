filename= 'jumsu.json'

myfile = open(filename,mode='rt',encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

humanList = list() #전체 결과를 저장할 리스트

import  json
jsonData = json.loads(mystring)
#type을 통해 어떤 형식인지 파악
print(type(jsonData))


for human in jsonData:
    name = human['name']
    print('이름 : %s'% name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    #upper 소문자를 대문자로 Downer 대문자 ->소문자
    _gender = human['gender'].upper()

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    print(type(human))
    message = '없음'

    if 'hello' in human.keys():
        message = human['hello']
        print('메시지:', message)
    else:
        message = '없음'
    mytuple = (name,kor,eng,math,total,gender,message)
    humanList.append(mytuple)

print(humanList)