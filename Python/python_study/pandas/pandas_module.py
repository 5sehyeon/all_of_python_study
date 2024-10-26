import pandas as pd
# Series (열이 하나)
print("----Serie----")
data = [10,30,10,-10]
series = pd.Series(data, index=["봄", "여름", "가을", "겨울"]) # 인덱스 번호말고 다른걸로 대체.
series.index.name = "계절" # 인덱스 이름 지정.
print(series)
print(series["봄"]) # "봄인덱스" 값 호출 (인덱스 호명,,)

# DataFrame (엑셀 형식)
print("----DataFrame (엑셀 형식)----")
data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}


df = pd.DataFrame(data)
print(df)

# 데이터 접근(column과 row)
print("----데이터 접근(column과 row)----")
print(df["이름"]) # 열(column) 하나 하나가 다 시리즈들이다 ! 
print(df["키"] > 190) # 각 행마다 열값의 T or F 를 리스트로 보여줌.
print(df["키"] - df["과학"]) # 한 행씩의 계산결과를 리스트로 보여줌.
a = df.columns # 열만 리스트로 묶임
print(df[a[0]])
print(df["이름"][0 : 3]) # 1st "이름" 열을 가져오고, 2nd 그중 위에서 0번째부터 2번째까지 짤라서 가져온다.
print(df.loc[0]) # 0번째 행을 가져온다.
print(df.loc[0, "수학"]) # 1st 0번째 행을 가져오고, 2nd 그중에서 "수학"열에 해당하는 데이터만 가져온다.(cell값)
print(df.loc[[0, 3], "키"]) # 1st 0번쨰 행과 3번쨰 행을 가져오는데, 2nd 그중에서 "키"열에 해당하는 데이터만 가져온다.(cell값)
print(df.loc[0 : 2, ["이름", "학교"]]) # 1st 0번째 행부터 1번째 행까지 가져오는데, 2nd "이름"과 "학교" 열에 해당하는 데이터들만 가져온다.
print(df.iloc[0, 5]) # row와 column을 인덱스 ""기본값""으로 호출한다.
print(df.iloc[[0 , 3], 2]) # 1st row 2nd column
print(df.iloc[0 : 3, [0, 1]])

# 데이터 확인
print("----데이터 확인----")
print(df.columns)
print(df.index)
print(df.shape) # (행x열) 크기
print(df.describe()) 
print(df["키"].sum())
print(df["키"].mean())
print(df["키"].nlargest())
print(df["학교"].unique())

# 데이터 선택(조건 == filter)                            # df[df[]] 구조 !!!!!
## 숫자에 적용한 필터링
print("----데이터 선택(조건 == filter)----")
print("----숫자에 적용한 필터링----")
filt = df["키"] > 185 
print(df[filt]) # 조건에 맞는 '행' 전체를 가져옴!! # df[] 문법에다가 넣어서, '열' 같지만 nope! # 필터링은 ""행""을 가져온다 !!!!!
print(df.loc[df["키"] > 185, "학교"]) # 1st 키가 185보다 큰 행들을 모두 가져오고,  2nd 열은 "학교"만 가져온다.
print(df[(df["키"] > 185) & (df["이름"].str.contains("태"))]) # 1st 키가 185보다 크고, 이름에 "태"가 들어간 행을 모두 가져온다.
print(df.loc[(df["키"] > 200) | (df["키"] < 170), "이름"]) # 1st 키가 200보다 크거나, 170보다 작은 행을 모두 가져오고, 2nd 그중 열은 "이름"만 가져온다.
## 문자열에 적용한 필터링
print("----문자열에 적용한 필터링----")
print(df[df["이름"].isin(["송태섭", "강백호"])]) # "이름" 열 값들중, "이름" 열 값이 ["송태섭" or "강백호"] 둘중 하나인 "행" 전체를 가져옴.
print(df.loc[df["이름"].str.contains("태"), "이름"]) # "이름" 열 값들중, "태" 가 들어간 값의 "행" 전체를 가져옴.


# 데이터 정렬
print("----데이터 정렬----")
print(df.sort_values("키", ascending=False)) # 키를 기준으로 데이터 정렬
print(df.sort_values(["영어", "수학"], ascending=[True, False])) # 1st 영어를 기준으로 오름차순, 2nd 만약 영어성적이 같을 경우, 수학 점수 내림차순으로
print(df.sort_index(ascending=True))

# 데이터 수정 
print("----데이터 수정----")
print(df["학교"].replace({"능남고" : "도봉고", "북산고" : "누원고"}, inplace=True)) # 1st "학교"열을 검사하고, 2nd 그증 능남고를 도봉고로, 북산고를 누원고로 바꾼다.
df["SW특기"] = df["SW특기"].str.capitalize() # 대문자로 바꿈
df["총합"] = df["국어"] + df["수학"] + df["영어"] + df["과학"] + df["사회"] # 열 추가
df["결과"] = "Fail" # 열 추가
df["외모"] = "잘생김" # 열 추가
df.loc[8] = ["오세현", "청원고", 182, 90, 90, 90, 90, 90, "Python", 450, "pass", "잘생김"] # 행 추가. loc[인덱스] #df.loc[8]은 df의 8행을 지칭한다.
print(df)
df.loc[df["총합"] > 400, "결과"] = "pass" # 조건에 맞는 특정 Cell값 수정.
df.loc[7, "이름"] = "오세현" # 특정 Cell값 수정.
print(df)
df.drop(columns="외모", inplace=True) # 열 삭제.
df.drop(index=8, inplace=True) # 행 삭제.
df = df[["이름", "학교", "키", "국어", "영어", "수학", "과학", "사회", "총합", "결과", "SW특기"]] # column 순서 변경. (df 재정의)

# 데이터 수정(함수적용)
print("----데이터 수정(함수적용)----")
def cm(키) : 
    return str(키) + "cm"
df["키"] = df["키"].apply(cm) # cm함수 인자로 "키"열에 해당하는 값들이 하나씩 들어온다.
print(df["키"])
print(df["키"].apply(len)) # len함수 인자로 "키"열에 해당하는 값들이 하나씩 들어온다.

# 결측치(NAN) 처리(.filla()함수와.dropna()함수)
print("----결측치(NAN) 처리(.filla()함수와.dropna()함수)-----")
df["SW특기"].fillna("없음", inplace=True) # "SW특기"열에 해당하는 값중, NUll 값이 있다면, "없음"으로 채워 넣는다.
df.fillna("없음", inplace=True)
df.dropna(axis="columns", how="any", inplace=True) # 열들중, Null 값이 하나라도 있는 열은 아예 삭제해버린다.
df.dropna(axis="index", how="all", inplace=True) # 행들중, 모든 값이 NUll인 행은 아예 삭제해버린다.


# Groupby
## 동일한 값을 가진 것들끼리 합쳐서, 통계 또는 평균등의 값을 계산하기 위해.
df_new = df.groupby("학교")["키"].min() # "학교"로 그룹을 묶은후, "키" 열만 뽑아, 그 평균값을 표현했다.
print(type(df_new)) # 인덱스 이름이 "학교"이고, 각 인덱스 번호가 "학교" 이름으로 바뀌고, 0번째 열이 키의 평균값이다. [Series]
print(df_new)

# Loops
print("----Loops----")
## df.groupyby() 의 경우
print("----df.groupyby() 의 경우----")
for school, dataframe in df.groupby("학교"):
    print(school)
    print(dataframe)

## df.index 의 경우
print("----df.index 의 경우----")
for i in df.index:
    print(i)

## df.iterrows() 의 경우
print("----df.iterrows() 의 경우----")
for index, serise in df.iterrows():
    print(index)
    print(serise) # serise는 해당 "행" 정보이다.

# df.loc[]과 df[]의 차이
print("----df.loc[]과 df[]의 차이----")
print(type(df["키"])) # 열이 하나여서, 자료형이 Series이다
print(type(df.loc[0:9, "키"])) # 열이 하나 ! Series ! 
print(type(df.loc[0 : 9, ["이름", "키"]])) # 열이 2개 이상이 되는 순간 Series의 합이 되어, 자료형이 DataFrame이다.

# Zip으로 Series 묶어서, DataFrame으로 만들기
print("----Zip으로 Series 묶어서, DataFrame으로 만들기----")
s1 = df["이름"]
s2 = df.loc[0:9, "키"]
new_df= pd.DataFrame(zip(s1, s2), columns=["이름", "키"])
print(new_df)

# DataFrame에 Series 추가하기 == DataFrame에 열하나 추가하기
print("----DataFrame에 Series 추가하기 == DataFrame에 열하나 추가하기----")
df1 = df.loc[0:9, ["이름", "키"]]
s1 = df["학교"]
print(s1)
df1["학교"] = s1 # 열 하나 생성 !!
print(df1)

# 인덱스 이름 바꾸기(index,,row,,column)
print("----인덱스 이름 바꾸기(index,,row,,column)----")
df = pd.DataFrame(data, index=["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번"]) # 인덱스 이름을 설정 !
df.index.name = "지원번호" # 인덱스 타이틀 설정 !
print(df)
df.reset_index(drop= True, inplace=True) # 인덱스 초기화. # inplace를 True로 해야지 실제 데이터가 바뀐다.
print(df)
'''
# dataframe을 excel, csv 파일로 생성+저장
df.to_excel("doo/연습1.xlsx")
df.to_csv("doo/연습2.csv", encoding="UTF-8-sig")

# excel, csv 파일을 dataframe 객체로 불러오기
df = pd.read_excel("doo/연습1.xlsx") # df는 똑같은 DataFrame이다.
df_new1 = df.head() # 처음 5행만 가져온다.
df_new2 = df.head(7) # df_new에는 첫 7행 까지의 데이터프레임이 담긴다.

data2 = {"sex" : ["man", "woman","man"],
         "name" : ["tom", "lisa", "paul"]}

df2 = pd.DataFrame(data2)
print(df2)

df2 = pd.get_dummies(df2)
print(df2)
'''


