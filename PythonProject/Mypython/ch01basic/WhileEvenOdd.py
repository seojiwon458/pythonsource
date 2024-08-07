odd, even = 0 ,0 #변수 선언 = odd는0 even은 0
i =1
while i <11:
    if i%2 ==0:
        even += i #짝수면 짝수인 i들을 더하고
    else:
        odd += i #짝수가 아닌 i들을 더함
    i+=1 #i가 1씩 커지는 구문

print('짝수의 총합 : %d'%even)
print('홀수의 총합 : %d'%odd)
#end while