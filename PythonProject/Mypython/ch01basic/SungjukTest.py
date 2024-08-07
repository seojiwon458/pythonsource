
def sungjuckInfo(name,kor,eng = 50,math = 60):
    total = kor + eng + math
    average = total/3.0

    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'

    print('%s 학생의 정보')
    print('국어 : %d, 영어 : %d , 수학 : %d' %(kor,eng,math))
    print('총점 : %d, 평균 : %.2f , 합격여부 : %s' % (total, average, passOrFail))

name,kor, eng,math = '김철수',50,60,70
sungjuckInfo(name,kor,eng,math) #positional argument
sungjuckInfo('박영희',80,) #positional argument

sungjuckInfo(math=30, eng=90,name='심현철',kor=100) #keyword argumnet
sungjuckInfo('권유정',50, math=70) #혼합은 포지션이 먼저 키워드가 나중으로 온다