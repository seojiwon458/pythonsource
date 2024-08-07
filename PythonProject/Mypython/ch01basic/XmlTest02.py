from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {'hong':('홍길동',60,80,70),
          'park':('박영희',50,70,95)
}
print(mydict)

xmlData = Element('students') # 루트 엘리먼트

for key, mytuple in mydict.items():
    # print(key)
    # print(mytuple)
    saram = SubElement(xmlData,'student')
    saram.attrib['id'] = key
    total = mytuple[1] + mytuple[2] + mytuple[3]
    average = total/3
    saram.attrib['평균'] = '%.3f' %average

    SubElement(saram, '이름').text = mytuple[0]
    SubElement(saram, '국어').text = str(mytuple[1])
    SubElement(saram, '영어').text = str(mytuple[2])
    SubElement(saram, '수학').text = str(mytuple[3])
# end def

def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end for

indent(xmlData)



xmlFile = 'xmlTest_02.xml'
ElementTree(xmlData).write(xmlFile,encoding='UTF-8')
print(xmlFile+' 파일이 생성되었습니다.')
