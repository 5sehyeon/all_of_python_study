import re
with open("C:/Users/djdjd/OneDrive/바탕 화면/Python/python_cafe/연습.txt","r",encoding="UTF-8") as f:
    text = f.read().replace("\n", " ")
    pattern_1 = r'민트 초코'
    pattern_2 = r'초코 민트'
    match = re.sub(pattern_1,"민트초코",text)
    match = re.sub(pattern_2,"초코민트",match)
    print(match)
    
    
    pattern_3 = r'싸모'
    pattern_4 = r'싸모님님'
    match = re.sub(pattern_3,"싸모님",match)
    match = re.sub(pattern_4,"싸모님",match)
    pattern_5 = r'신영'
    print(match)
    