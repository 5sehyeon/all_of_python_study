import re

class Document:
    # self를 이용한 클래스 내부 변수 선언 (state)
    def __init__(self, file):
        self.file = file
        with open(self.file, "r", encoding="UTF-8") as f:
            text = f.read().split()
            self.text = text
            dic = {}
            self.dic = dic
            for i in self.text:
                token = re.sub(r'\W+', '', i.lower())
                if token in dic.keys():
                    dic[token] += 1
                elif token not in dic.keys():
                    dic[token] = 1
    
    # 메서드(함수)
    def term_frequency(self, word):
        count = 0
        for i in self.text:
            token = re.sub(r'\W+', '', i.lower())
            if token == word:
                count += 1
                
        result = (count / len(self.text))
        return result
    
    def get_word(self):
        return list(self.dic.keys())