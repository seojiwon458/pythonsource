humanDict = {
    'age':20, 'name':'유현식', 'hobby':'독서',
    'address' : {'city':'seoul','gu':'마포구','zipcode':'12345'}
}
print(type(humanDict))
print(humanDict)

import json
humanString = json.dumps(humanDict,ensure_ascii=False,indent=4,sort_keys=True)
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString)
print('이름 : %s' %humanJson['name'],
      '취미 : %s' %humanJson ['hobby'],
      '나이 : %s' %humanJson ['age'],
      '주소 : %s' %humanJson ['address']['city'],
      '구 : %s' %humanJson ['address']['gu'],
      'Zipcode : %s' %humanJson ['address']['zipcode'])
