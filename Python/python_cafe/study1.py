from konlpy.tag import Okt
from data import data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,jansu,menu
import os
import konlpy
import zipfile

okt = Okt()

for i in range(2):  # 마지막엔 해당 파일을 삭제 해야한다..
    konlpy_path = os.path.dirname(konlpy.__file__)
    java_path = os.path.join(konlpy_path, "java")
    os.chdir(java_path)
    os.getcwd()
        
    jar_file_path = 'open-korean-text-2.1.0.jar'
        
    with zipfile.ZipFile(jar_file_path, 'r') as jar:
        jar.extractall()
            
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", "r", encoding="UTF-8") as f:
        data = f.read()
    
    data += data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + jansu + menu + data11
        
    with open("C:/Users/djdjd/AppData/Local/Programs/Python/Python312/Lib/site-packages/konlpy/java/org/openkoreantext/processor/util/noun/names.txt", 'w', encoding="UTF-8") as f:
        f.write(data)
    data


print(okt.pos("경욱삼촌에게")) # 경욱 미선 장미애 김미애 윤자이모 중열삼촌 쭈이모 찬서("이"를 붙이는 경우,, 서인이형)
print(okt.pos("세현 베리고 1잔 부탁드립니다."))
print(okt.pos("오트밀 베리고 한잔 부탁드립니다."))
print(okt.pos("유빈 오트밀베리고 1잔 부탁해요"))

menu1 = ["베리고", "아아"]

for i in ["오트밀 베리고 한잔 부탁드립니다.", "세현 베리고 1잔 부탁드립니다.", "아아 1", "유빈 오트밀베리고 1잔 부탁해요"]:
    pos_tags = okt.pos(i)
    result = [word for word, pos in pos_tags if pos in ["Noun", "Josa", "Number"]]
    if list(set(result)&set(menu1)).pop(0) in menu1:
        print("예")


print(okt.pos("김싸리양" ))

for i in range(10):
    if i == 3:
        print('ㅎㅎ')
        break
    else:
        pass