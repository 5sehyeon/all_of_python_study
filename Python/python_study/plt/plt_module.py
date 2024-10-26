# Matplotlib (그래프)
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns


# 한글폰트와 글씨크기
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows, 한글
matplotlib.rcParams['font.size'] = 15 # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False

# Title설정
plt.title("꺽은선 그래프")
plt.plot([-1, 0, 1], [-5, -1, 2]) # 메인 함수그래프.
plt.show()

# 축
x = [1, 2, 3] 
y = [2 ,4, 8]
# (1,2), (2,4), (3,8)을 지나는 함수.
plt.plot(x, y)
plt.xticks(range(0,101,10)) # 눈금
plt.yticks(range(0,101,10)) # 눈금
plt.xlabel("x축", color="red", loc="right")
plt.ylabel("y축", loc="top")
plt.show()

# 범례(legend)
plt.plot(x,y, label="무슨 데이터") # 그래프가 뭘 의미하는 지,,
plt.legend(loc="lower right")
plt.show()

# 스타일
plt.plot(x,y,marker="o", markersize=4, linestyle="None")
plt.show()

# 선 스타일
plt.plot(x,y,linestyle="--",color="blueviolet") # 선 색깔 변경.
plt.show()

# 포맷
plt.plot(x,y, "ro--") #color, marker, linestyle
plt.show()

# 그래프 크기(figsize)
plt.figure(figsize=(10,5), dpi=200, facecolor="#EFB55E") # dpi는 dots per inch(확대)
plt.plot(x,y)
plt.show()

# 파일저장
plt.plot(x,y)
plt.savefig("doo/graph.png", dpi=100)

# 텍스트 넣기
plt.plot(x,y,marker="o")
for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.1, txt, ha="center", color="blue") # x좌표 y좌표 y값 표시
plt.show()


# 여러 데이터 넣기(함수)
plt.plot(x, y)
days = [1, 2, 3]
az = [2, 4, 8]
pfizer = [5, 1, 3]
moderna = [1, 2, 5]

plt.plot(days, az, label="az")
plt.plot(days, pfizer, label="pfizer", marker="o", ls="--") # 그래프에 대한 모든것. "좌표,라인스타일,라인색깔,점마커,그래프 설명"
plt.plot(days, moderna, label="moderna", marker="s", ls="-")
plt.ylim(0.5, 9)
plt.legend(ncol=3)
plt.show()

# 막대그래프(기본)
labels = ["강백호", "서태웅", "정대만"] # x
values = [190, 187, 184] # y
colors = ["r", "g", "b"]
plt.bar(labels, values, color=colors, width=0.1) # x와 y 개념 !!
plt.xticks(rotation=45, ticks=["1번", "2번", "3번"]) # 45도 기울림
plt.ylim(175,195) #y축의 데이터 제한. 더 자세히 보여줌
plt.show()

# dataframe 활용
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
plt.plot(df["이름"], df["키"])
plt.plot(df["이름"], df["수학"])
plt.grid()
plt.show()


# 다중 그래프
import numpy as np
N = df.shape[0]
index = np.arange(N)
w = 0.25
plt.figure(figsize=(10,5))
plt.title("학생들 성적")
plt.bar(index - w, df["국어"], width=0.25, label="국어")
plt.bar(index, df["영어"], width=0.25, label="영어")
plt.bar(index + w, df["수학"], width=0.25, label="수학")
plt.legend()
plt.xticks(index, df["이름"], rotation=60)
plt.show()

# 산점도
plt.scatter(df["영어"], df["수학"]) # 산점도 x, y 개념 !!
plt.xlabel("영어 점수")
plt.ylabel("수학 점수")
plt.show()

# 여러 그래프
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
axs[0, 0].plot()
plt.show()

