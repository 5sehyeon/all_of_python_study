import re

# re모듈의 함수들
text = "사과 한개의 가격은 $2.45달러 입니다. (사과는 진짜 맛있어요.) 배는 $200달러입니다."
pattern_1 = "사과"

# match 함수(시작부분만 패턴과 일치해면, 시작부분 패턴을 잡아줌)
match_1 = re.match(pattern_1,text)
print(match_1, match_1.group())
# fullmatch 함수(시작부터 끝까지 패턴과 일치해야지만, 패턴을 잡아줌) 
match_2 = re.fullmatch(pattern_1,text)
print(match_2)
# search 함수(텍스트 어디에 있던, 패턴과 일치하는 부분이 존재하면, 잡아줌) (중복될 경우, 첫 번째 단어만 가져옴)
match_3 = re.search(pattern_1,text)
print(match_3, match_3.group())
# findall 함수(search함수에서 더 나아가서, 패턴에 부합하는 '모든' 부분들을 '모두' 가져와서 뱉어줌)
match_4 = re.findall(pattern_1,text)
print(match_4)
# sub 함수(패턴에 부합하는 모든 부분들을 새로운 문자로 모두 바꿔준다.) (문자열로 바꿔야 한다 !)
match_5 = re.sub(pattern_1, "배", text)
print(match_5)


# re모듈의 매크로들
pattern_2 = r'\d' #텍스트 내에 존재하는 '모든' 숫자를 하나하나 끊어서 뽑아낸다
pattern_3 = r'(\d+)'#택스트 내에 존재하는 '모든' 숫자를 띄어쓰기 단위로 묶어서 뽑아낸다 ('+'의 역할)
print(re.findall(pattern_2,text),re.findall(pattern_3,text))
pattern_4 = r'\s' #택스트 내에 존재하는 '모든' 공백문자를 뽑아낸다
print(re.findall(pattern_4,text))
pattern_5 = r'^사과' #택스트 내에서 '사과'로 시작하면, '사과'를 뽑아낸다
print(re.findall(pattern_5,text))
pattern_6 = r'배$' #택스트 내에서 '배'로 끝나면, '배'를 뽑아낸다
pattern_7 = r'사과|배' #택스트 내에서 '사과'혹은 '배'가 있으면 '모두' 뽑아낸다.
print(re.findall(pattern_7,text))
pattern_8 = r'\w' #공백문자 빼고, 모든 글자,숫자를 하나씩 뽑아낸다
pattern_9 = r'\w+' #공백문자 빼고, 모든 글자,숫자를 띄어쓰기 단위로 묶어서 뽑아낸다
print(re.findall(pattern_8,text),re.findall(pattern_9,text))

# (.*?)는 경계사이에 있는 모든 문자열들을 가지고 온다. (불확실한 문자열들을 지칭.)

# re모듈의 캡쳐그룹 ()에 묶여있는 부분을 전부 가져온다. ()가 없으면, 전체를 ()한 것과 동일게 본다. 전체를 캡쳐그룹으로 본다.
pattern_10 = r'에게(.*?)선물' 
pattern_11 = r'(에게.*?선물)' #r'에게.*?선물' == r'(에게.*?선물)' ()가 아예 없으면, 전체를 ()로 캡쳐 그룹으로 잡은 것이다. 디폴트 !!
pattern_12 = r'(\d+)원입니다' #'숫자+원입니다' 조합일 때만 잡아내지만, 실제 뽑아내는 것은 캡쳐 그룹인 앞에 있는 (숫자)만 뽑아낸다.
print(re.findall(pattern_10,"세현이에게 커피 4잔 선물합니다."),re.findall(pattern_11,"세현이에게 커피 4잔 선물합니다."))
print(re.findall(pattern_12,"사과 하나에 600원입니다."))

# re모듈의 범위지정
pattern_13 = r'\d{1,3}' #{}는 한번에 가져올 문자의 개수를 지정
print(re.findall(pattern_13,text))
pattern_14 = r'\((.*?)\)' # 모든 특수문자 자체를 말하고 싶으면 이스케이프문자(\)를 앞에 써줘야 한다.
print(re.findall(pattern_14,text))

# r' '에 문자대신 변수는 상황
a = "사과"
pattern_15 = fr'{a} (한개)' # 요런 어구와 일치할 때, '한개'만 뽑아낸다.
print(re.findall(pattern_15,text))

# 한 패턴안에 캡쳐그룹이 여러개 있을 경우, 튜플로 묶인다.
print(re.findall(r'(아아).*?(먹어요)', "아아 하나 먹어요 아아 두개 먹어요"))

# 실제 예시
pattern_16 = r'(\d{4})-(\d{2})-(\d{2})' # 요런 어구의 상황과 일치할 때, 캡쳐그룹만 뽑아온다!!!
print(re.findall(pattern_16,"2024-10-26일에 작성"))
pattern_17 = r'(\[.*?\])'
print(re.findall(pattern_17,"[오세현][오전 10:26] 아아 하나 먹어요"))
