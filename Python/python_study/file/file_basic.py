import re

with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_study/file/test.txt","r",encoding="UTF-8") as f:
    print(f) # 정보출력
    # f = f.readlines() 한줄씩(\n)포함, 리스트로 묶인 상태
    text = f.read().replace("\n", " ")
    print(text)
    text_line_list = text.split(" [")
    print(text_line_list)
    
with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_study/file/test.txt","r",encoding="UTF-8") as f2:
    text = f2.read().replace("\n"," ")
    pattern = r"\{(.*?)\}"
    filt_text = re.findall(pattern,text)
    print(filt_text)
    
    
    