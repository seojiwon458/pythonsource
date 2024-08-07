coffee01 = ('아메리카노','카페라뗴')
coffee02 = ('콜드브루','아이스커피')

#요소들을 콤마로 연결하면,Tuple로 인식합니다
# ,가 나오면 Tuple이다
coffee03 = '카푸치노','마끼야또'

mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼','플랫화이트']
coffee04 = tuple(mylist) #리스트를 튜플로 변환

#튜플하고 문자는 합칠수 없다
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
#파이썬 요소 구할때 len사용
length = len(coffees)
print('요소 개수: %d' %length)
print(type(coffees))
print(coffees)

#인덱싱과 슬라이싱
print('앞에서 3번째 요소:%s'%coffees[3])
print('뒤에서 2번째 요소 %s'%coffees[-2])

print('1번째부터 3번째까지의 요소들 %s', end = '')
print(coffees[1:4])

print('4번째이후 요소들 %s', end = '')
print(coffees[4:])

print('3번째까지의 요소들 %s', end = '')
print(coffees[:4])

mycount = coffees.count('아메리카노')
print(mycount)

#파이썬은 없는게 들어가면 자바와 다르게 예외처리한다.
#myindex = coffees.index('호호호')
#print(myindex)

x,y = 3,4
print('before x: %d y :%d' %(x,y))

#파이썬의 Swap
x,y = y,x
print('after x: %d y :%d' %(x,y))