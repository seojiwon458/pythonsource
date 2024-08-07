def girlFreiendCheck(findName):
    girlFreiend = ['은하','소원','유주','예린',' 신비','엄지']
    isMember = findName in girlFreiend

    if isMember:
        message ='\' %s\' 님은 여자친구 멤버가 입니다.' %findName
        print(message)
    else:
        meessage =  message ='\' %s\' 님은 여자친구 멤버가 아닙니다.' %findName
        raise  Exception (meessage)

name = '윤종신'

try:
    girlFreiendCheck(name)
except Exception as err:
    print('예외 발생 : {}'.format(err))