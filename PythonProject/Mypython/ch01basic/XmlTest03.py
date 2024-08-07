from xml.etree.ElementTree import parse

tree = parse(source = 'Car_info.xml')

myroot = tree.getroot();
print(type(myroot))

carList = myroot.findall('car')
print(type(carList))
print('총 car 수 : %d '%len(carList))

for currCar in carList:
    print('car 구성 정보')
    brand = currCar[0].text
    brandName = currCar[0].attrib['name']
    Model = currCar[1].text
    Year = currCar[2].text
    Color = currCar[3].text


    print('브랜드 : %s' %(brand))
    print('브랜드 이름: %s' % (brandName))
    print('모델: %s' % (Model))
    print('출시년도: %s' % (Year))
    print('색상: %s' % (Color))

    print('-'*30)