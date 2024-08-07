def add(first,second):
    return first + second

su01 = 14
su02 = 5

result = add(su01,su02) #위치기반 positional argument
print('%d + %d = %d' %(su01,su02,result))

result = add(first=10.,second=20) #키워드기반 keyword argument
print('%d + %d = %d' %(10,20,result))

result = add(100,200)
print('%d + %d = %d' %(100,200,result))