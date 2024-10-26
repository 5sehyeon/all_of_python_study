import pandas as pd
import csv
import re
import openpyxl 

 # 5.2일 알고리즘 시험 완료..시범운용가능상태.. 정준 넣기, 이름이 긴 단체 알고리즘 추가
 # 해야할 것들: 인식 가능한 맨트들 추가, 메뉴판 적기, 이름이 긴 팀단위 알고리즘에 추가.
 # 버전 업그레이드를 위한 생각: 문자열안에 포맷문자 생각해보기,,대화 하나하나를 읽는 알고리즘 생각해보기,,엄마 아빠 매칭(2세한테.),,어르신 = 신종훈 목사님 = 대표님, 위상무 = 위세량 오봉 = 오봉엽, 산양 = 선영, 
 # 새로 오신 분 넣기, 섭드립을 포함한 메뉴 정리, 공동체 손님 넣기


with open("C:/Users/오세현/OneDrive/바탕 화면/버전1시험 최종 카톡내용.txt", "r", encoding="UTF-8") as f:
    
    
    
    file_path = "C:/Users/오세현/OneDrive/바탕 화면/카페_3_4월.xlsx"
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    sheet = workbook["정산"]

    
    # 딕셔너리로 이름과 항목별 돈을 정리.
    dic1 = {"은경" : [0, 0, 0, 0, 0], "상준" : [0, 0, 0, 0, 0], "유빈" : [0, 0, 0, 0, 0], "유진" : [0, 0, 0, 0, 0], "은미" : [0, 0, 0, 0, 0], "규열" : [0, 0, 0, 0, 0], "남현" : [0, 0, 0, 0, 0], "미선" : [0, 0, 0, 0, 0], "김미" : [0, 0, 0, 0, 0],
            "미정" : [0, 0, 0, 0, 0], "보라" : [0, 0, 0, 0, 0], "보미" : [0, 0, 0, 0, 0], "서인" : [0, 0, 0, 0, 0], "선애" : [0, 0, 0, 0, 0], "소리" : [0, 0, 0, 0, 0],"김아아인": [0,0,0,0,0],"영민" : [0, 0, 0, 0, 0], "유신" : [0, 0, 0, 0, 0], "자애" : [0, 0, 0, 0, 0],
            "정연" : [0, 0, 0, 0, 0], "정옥" : [0, 0, 0, 0, 0], "중열" : [0, 0, 0, 0, 0], "하연" : [0, 0, 0, 0, 0], "김향" : [0, 0, 0, 0, 0], "김호" : [0, 0, 0, 0, 0], "제원" : [0, 0, 0, 0, 0], "승규" : [0, 0, 0, 0, 0], "찬서" : [0, 0, 0, 0, 0],
            "채원" : [0, 0, 0, 0, 0], "미소" : [0, 0, 0, 0, 0], "목사님" :[0, 0, 0, 0, 0], "민희" : [0, 0, 0, 0, 0], "서희" : [0, 0, 0, 0, 0], "세범" : [0, 0, 0, 0, 0], "제인" : [0, 0, 0, 0, 0], "지우" : [0, 0, 0, 0, 0], "윤희" : [0, 0, 0, 0, 0],
            "혜린" : [0, 0, 0, 0, 0], "박혜" : [0, 0, 0, 0, 0], "환희" : [0, 0, 0, 0, 0], "예진" : [0, 0, 0, 0, 0], "진수" : [0, 0, 0, 0, 0], "진영" : [0, 0, 0, 0, 0], "철환" : [0, 0, 0, 0, 0], "싸모님" : [0, 0, 0, 0, 0], "윤구" : [0, 0, 0, 0, 0],
            "윤지" : [0, 0, 0, 0, 0], "주리" : [0, 0, 0, 0, 0], "다진" : [0, 0, 0, 0, 0], "보영" : [0, 0, 0, 0, 0], "연정" : [0, 0, 0, 0, 0], "정화" : [0, 0, 0, 0, 0], "병근" : [0, 0, 0, 0, 0], "종훈" : [0, 0, 0, 0, 0], "지온" : [0, 0, 0, 0, 0],
            "수현" : [0, 0, 0, 0, 0], "안지" : [0, 0, 0, 0, 0], "지훈" : [0, 0, 0, 0, 0], "경욱" : [0, 0, 0, 0, 0], "봉엽" : [0, 0, 0, 0, 0], "세현" : [0, 0, 0, 0, 0], "완택" : [0, 0, 0, 0, 0], "오쭈" : [0, 0, 0, 0, 0], "준영" : [0, 0, 0, 0, 0],
            "윤보라" : [0, 0, 0, 0, 0],"세량" : [0, 0, 0, 0, 0], "한나" : [0, 0, 0, 0, 0], "한비" : [0, 0, 0, 0, 0], "까루나" : [0, 0, 0, 0, 0], "동하" : [0, 0, 0, 0, 0], "상원" : [0, 0, 0, 0, 0], "서은" : [0, 0, 0, 0, 0], "선영" : [0, 0, 0, 0, 0],
            "승엽" : [0, 0, 0, 0, 0], "영섭" : [0, 0, 0, 0, 0], "은혜" : [0, 0, 0, 0, 0], "익희" : [0, 0, 0, 0, 0], "주원" : [0, 0, 0, 0, 0], "이쭈" : [0, 0, 0, 0, 0], "지연" : [0, 0, 0, 0, 0], "충희" : [0, 0, 0, 0, 0], "혜원" : [0, 0, 0, 0, 0], 
            "성은" : [0, 0, 0, 0, 0], "순환" : [0, 0, 0, 0, 0], "지윤" : [0, 0, 0, 0, 0], "서윤" : [0, 0, 0, 0, 0], "미성" : [0, 0, 0, 0, 0], "장미" : [0, 0, 0, 0, 0], "재순" : [0, 0, 0, 0, 0], "진실" : [0, 0, 0, 0, 0], "호중" : [0, 0, 0, 0, 0],
            "민율" : [0, 0, 0, 0, 0], "정설" : [0, 0, 0, 0, 0], "성하" : [0, 0, 0, 0, 0], "승민" : [0, 0, 0, 0, 0], "아인" : [0, 0, 0, 0, 0],"영경" : [0, 0, 0, 0, 0], "우신" : [0, 0, 0, 0, 0], "원영" : [0, 0, 0, 0, 0], "은수" : [0, 0, 0, 0, 0], 
            "정준" : [0, 0, 0, 0, 0], "정지" : [0, 0, 0, 0, 0], "진호" : [0, 0, 0, 0, 0], "현아" : [0, 0, 0, 0, 0], "혜영" : [0, 0, 0, 0, 0],"다인" : [0, 0, 0, 0, 0], "영준" : [0, 0, 0, 0, 0], "주혜" :[0, 0, 0, 0, 0],"쿄타" : [0, 0, 0, 0, 0], "선경" : [0, 0, 0, 0, 0], "윤미" : [0, 0, 0, 0, 0], 
            "종문" : [0, 0, 0, 0, 0], "종윤" : [0, 0, 0, 0, 0], "선화" : [0, 0, 0, 0, 0], "성욱" : [0, 0, 0, 0, 0], "지희" : [0, 0, 0, 0, 0], "규온" : [0, 0, 0, 0, 0], "하원" : [0, 0, 0, 0, 0], "하루" : [0, 0, 0, 0, 0], "하루나" : [0, 0, 0, 0, 0],
            "하이" : [0, 0, 0, 0, 0], "홍" : [0, 0, 0, 0, 0], "싸리" : [0, 0, 0, 0, 0], "츄츄" : [0, 0, 0, 0, 0], "찰스" : [0, 0, 0, 0, 0], "단디" : [0, 0, 0, 0, 0], "정진" : [0, 0, 0, 0, 0],
            "진선" : [0, 0, 0, 0, 0], "데이빗" : [0, 0, 0, 0, 0], "윤자" : [0 ,0, 0, 0, 0], "금자" : [0, 0, 0, 0, 0], "장호" : [0, 0, 0, 0, 0], "앙상블" : [0, 0, 0, 0, 0], "거숨" : [0, 0, 0, 0, 0], "봉독대" : [0, 0, 0, 0, 0], "연극모임" : [0, 0, 0, 0, 0], 
            "글쓰기모임" : [0, 0, 0, 0, 0], "안골청연" : [0, 0, 0, 0, 0], "농사팀" : [0, 0, 0, 0, 0], "숨" : [0, 0, 0, 0, 0], "휴먼스" : [0, 0, 0, 0, 0], "교사페이" : [0, 0, 0, 0, 0], "알바부족" : [0, 0, 0, 0, 0], "오늘교육원" : [0, 0, 0, 0, 0], "데코팀" : [0, 0, 0, 0, 0], 
            "스텝팀" : [0, 0, 0, 0, 0], "캐나다섬김팀" : [0, 0, 0, 0, 0], "공동체손님" : [0, 0, 0, 0, 0], "1부족" : [0, 0, 0, 0, 0], "2부족" : [0, 0, 0, 0, 0], "3부족" : [0, 0, 0, 0, 0], "4부족" : [0, 0, 0, 0, 0], "5부족" : [0, 0, 0, 0, 0], "6부족" : [0, 0, 0, 0, 0],
            "7부족" : [0, 0, 0, 0, 0],
            "향" : [0, 0, 0, 0, 0], "향이" : [0, 0, 0, 0, 0], "향누" : [0, 0, 0, 0, 0], "향언" : [0 ,0, 0, 0, 0],  "향에" : [0 ,0, 0, 0, 0], "향한" : [0 ,0, 0, 0, 0], "향님" : [0 ,0, 0, 0, 0],
            "호" : [0, 0, 0, 0, 0], "호오" : [0, 0, 0, 0, 0], "호삼" : [0, 0, 0, 0, 0], "호형" : [0 ,0, 0, 0, 0],  "호에" : [0 ,0, 0, 0, 0], "호한" : [0 ,0, 0, 0, 0], "호님" : [0 ,0, 0, 0, 0],
            "대표님" : [0 ,0, 0, 0, 0],
            "연화" : [0 ,0, 0, 0, 0],
            "싸모" : [0 ,0, 0, 0, 0], "사모" : [0, 0, 0, 0, 0],
            "설" : [0 ,0, 0, 0, 0], "설오" : [0 ,0, 0, 0, 0], "설삼" : [0 ,0, 0, 0, 0], "설형" : [0 ,0, 0, 0, 0],  "설에" : [0 ,0, 0, 0, 0], "설한" : [0 ,0, 0, 0, 0], "설님" : [0 ,0, 0, 0, 0],
            "홍" : [0 ,0, 0, 0, 0], "홍이" : [0 ,0, 0, 0, 0], "홍누" : [0 ,0, 0, 0, 0], "홍언" : [0 ,0, 0, 0, 0],  "홍에" : [0 ,0, 0, 0, 0], "홍한" : [0 ,0, 0, 0, 0], "홍님" : [0 ,0, 0, 0, 0],
            "준이" : [0 ,0, 0, 0, 0]}
                #   내 먹  주 받 남
    
    dic2 = {"한": 1, "하" : 1, "1":1, "두":2, "2":2, "세":3, "석":3, "3":3, "네":4, "4":4, "다" :5, "5":5, "여섯":6, "6":6, "일":7, "7":7, "잔":1}
    sum = {"매출" : 0}
    
                                                
                                                
    def ta_and_rec(num):
        dic1[ta][2] = dic1[ta][2] + (cup*3000)
        money = (cup*3000)
        while money > 0:
            if dic1[ta][4] > 0:
                dic1[ta][4] = dic1[ta][4] - 100
                money = money - 100
            elif dic1[ta][4] == 0:
                dic1[ta][0] = dic1[ta][0] + 100
                money = money - 100
        sum["매출"] = sum["매출"] + (cup*3000)
        if (rec == "하루") and (fittered_data[len(fittered_data)-num][2] == "나"):
            if dic1["하루나"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["하루나"][0] > 0:
                        dic1["하루나"][0] = dic1["하루나"][0] - 100
                        dic1["하루나"][3] = dic1["하루나"][3] + 100
                        money = money - 100
                    elif dic1["하루나"][0] == 0:
                        dic1["하루나"][4] = dic1["하루나"][4] + 100
                        dic1["하루나"][3] = dic1["하루나"][3] + 100
                        money = money - 100
            elif dic1["하루나"][0] == 0:
                dic1["하루나"][3] = dic1["하루나"][3] + (cup*3000)
                dic1["하루나"][4] = dic1["하루나"][4] + (cup*3000)
        elif rec == "까루":
            if dic1["까루나"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["까루나"][0] > 0:
                        dic1["까루나"][0] = dic1["까루나"][0] - 100
                        dic1["까루나"][3] = dic1["까루나"][3] + 100
                        money = money - 100
                    elif dic1["까루나"][0] == 0:
                        dic1["까루나"][4] = dic1["까루나"][4] + 100
                        dic1["까루나"][3] = dic1["까루나"][3] + 100
                        money = money - 100
            elif dic1["까루나"][0] == 0:
                dic1["까루나"][3] = dic1["까루나"][3] + (cup*3000)
                dic1["까루나"][4] = dic1["까루나"][4] + (cup*3000)
        elif rec == "데이":
            if dic1["데이빗"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["데이빗"][0] > 0:
                        dic1["데이빗"][0] = dic1["데이빗"][0] - 100
                        dic1["데이빗"][3] = dic1["데이빗"][3] + 100
                        money = money - 100
                    elif dic1["데이빗"][0] == 0:
                        dic1["데이빗"][4] = dic1["데이빗"][4] + 100
                        dic1["데이빗"][3] = dic1["데이빗"][3] + 100
                        money = money - 100
        elif rec == "목사":
            if dic1["목사님"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["목사님"][0] > 0:
                        dic1["목사님"][0] = dic1["목사님"][0] - 100
                        dic1["목사님"][3] = dic1["목사님"][3] + 100
                        money = money - 100
                    elif dic1["목사님"][0] == 0:
                        dic1["목사님"][4] = dic1["목사님"][4] + 100
                        dic1["목사님"][3] = dic1["목사님"][3] + 100
                        money = money - 100
            elif dic1["목사님"][0] == 0:
                dic1["목사님"][3] = dic1["목사님"][3] + (cup*3000)
                dic1["목사님"][4] = dic1["목사님"][4] + (cup*3000)
        elif rec == "대표":
            if dic1["대표님"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["대표님"][0] > 0:
                        dic1["대표님"][0] = dic1["대표님"][0] - 100
                        dic1["대표님"][3] = dic1["대표님"][3] + 100
                        money = money - 100
                    elif dic1["대표님"][0] == 0:
                        dic1["대표님"][4] = dic1["대표님"][4] + 100
                        dic1["대표님"][3] = dic1["대표님"][3] + 100
                        money = money - 100
            elif dic1["대표님"][0] == 0:
                dic1["대표님"][3] = dic1["대표님"][3] + (cup*3000)
                dic1["대표님"][4] = dic1["대표님"][4] + (cup*3000)
        elif rec == "싸모":
            if dic1["싸모님"][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1["싸모님"][0] > 0:
                        dic1["싸모님"][0] = dic1["싸모님"][0] - 100
                        dic1["싸모님"][3] = dic1["싸모님"][3] + 100
                        money = money - 100
                    elif dic1["싸모님"][0] == 0:
                        dic1["싸모님"][4] = dic1["싸모님"][4] + 100
                        dic1["싸모님"][3] = dic1["싸모님"][3] + 100
                        money = money - 100
            elif dic1["싸모님"][0] == 0:
                dic1["싸모님"][3] = dic1["싸모님"][3] + (cup*3000)
                dic1["싸모님"][4] = dic1["싸모님"][4] + (cup*3000)
            
        else:
            if dic1[rec][0] > 0:
                money = cup*3000
                while money>0:
                    if dic1[rec][0] > 0:
                        dic1[rec][0] = dic1[rec][0] - 100
                        dic1[rec][3] = dic1[rec][3] + 100
                        money = money - 100
                    elif dic1[rec][0] == 0:
                        dic1[rec][4] = dic1[rec][4] + 100
                        dic1[rec][3] = dic1[rec][3] + 100
                        money = money - 100
            elif dic1[rec][0] == 0:
                dic1[rec][3] = dic1[rec][3] + (cup*3000)
                dic1[rec][4] = dic1[rec][4] + (cup*3000)
            
    
    def menu_def1(m):
        money = (m*cup)
        while money > 0:
            if dic1[ta][4] > 0:
                dic1[ta][4] = dic1[ta][4] - 100
                dic1[ta][1] = dic1[ta][1] + 100
                money = money - 100
            elif dic1[ta][4] == 0:
                dic1[ta][0] = dic1[ta][0] + 100
                dic1[ta][1] = dic1[ta][1] + 100
                money = money - 100
        sum["매출"] = sum["매출"] + (m*cup)
    
    
    def menu_def2(m):
        money = (m*int(fittered_data[l+1][0]))
        while money > 0:
            if dic1[ta][4] > 0:
                dic1[ta][4] = dic1[ta][4] - 100
                dic1[ta][1] = dic1[ta][1] + 100
                money = money - 100
            elif dic1[ta][4] == 0:
                dic1[ta][0] = dic1[ta][0] + 100
                dic1[ta][1] = dic1[ta][1] + 100
                money = money - 100
        sum["매출"] = sum["매출"] + (m*int(fittered_data[l+1][0]))
        
                    
                    
    # 본격적으로 파일을 읽고 처리하는 부분시작.  ta는 선물주는 사람, rec는 선물받는 사람 cup은 잔 수
    for i in f:
        i = i.split()
        fittered_data = []
        for word in i:
            fittered_word = re.sub(r'\W+', '', word)
            fittered_data.append(fittered_word)
        count = 2
        # 1번 알고리즘(선물하는 경우)
        if ("선물합니다" in fittered_data) or ("선물해요" in fittered_data) or ("선물합니당" in fittered_data) :
            if ("선물합니다" in fittered_data):
                b = fittered_data.index("선물합니다")
            elif ("선물해요" in fittered_data):
                b = fittered_data.index("선물해요")
            elif ("선물합니당" in fittered_data):
                b = fittered_data.index("선물합니당")
            for j in range(b+1, len(fittered_data)):
                fittered_data.remove(fittered_data[b+1])
            if "섬김이분들께" in fittered_data:
                kind = fittered_data[(len(fittered_data)-5)]
                lst = input(f"{kind} 섬김이들 이름을 입력하시오:") 
                lst = lst.split(" ")
                ta = fittered_data[0][1:3]
                cup = dic2[fittered_data[(len(fittered_data)-2)][0]]
                if ta == "이빗":
                    ta = "데이빗"
                elif ta == "루나":
                    ta = "하루나"
                elif ta == "경현":
                    ta = "까루나"
                elif ta == "사님":
                    ta = "목사님"
                elif ta == "모님":
                    ta = "싸모님"
                elif ta == "향":
                    ta = "김향"
                elif ta == "호":
                    ta = "김호"
                elif ta == "설":
                    ta = "정설"
                elif ta == "이":
                    ta = "하이"
                elif ta == "정현":
                    ta = "홍"
                elif ta == "미애":
                    if fittered_data[0][0] == "장":
                        ta = "장미"
                    elif fittered_data[0][0] == "김":
                        ta = "김미"         
                elif ta == "주현":
                    if fittered_data[0][0] == "이":
                        ta = "이쭈"
                    elif fittered_data[0][0] == "오":
                        ta = "오쭈"
                elif ta == "혜인":
                    if fittered_data[0][0] == "박":
                        ta = "박혜"
                    elif fittered_data[0][0] == "주":
                        ta = "주혜"
                elif ta == "지현":
                    if fittered_data[0][0] == "안":
                        ta = "안지"                 
                    elif fittered_data[0][0] == "정":
                        ta = "정지"
                dic1[ta][2] = dic1[ta][2] + (3000*cup*len(lst))
                money = (3000*cup*len(lst))
                while money > 0:
                    if dic1[ta][4] > 0:
                        dic1[ta][4] = dic1[ta][4] - 100
                        money = money - 100
                    elif dic1[ta][4] == 0:
                        dic1[ta][0] = dic1[ta][0] + 100
                        money = money - 100
                sum["매출"] = sum["매출"] + (3000*cup*len(lst))
                for h in lst:
                    dic1[h][3] = dic1[h][3] + (3000*cup)
                    dic1[h][4] = dic1[h][4] + (3000*cup)
            else:
                rec = fittered_data[len(fittered_data)-4][0:2]
                ta = fittered_data[0][1:3]
                if ta == "이빗":
                    ta = "데이빗"
                elif ta == "루나":
                    ta = "하루나"
                elif ta == "경현":
                    ta == "까루나"
                elif ta == "사님":
                    ta = "목사님"
                elif ta == "모님":
                    ta = "싸모님"
                elif ta == "향":
                    ta = "김향"
                elif ta == "호":
                    ta = "김호"
                elif ta == "설":
                    ta = "정설"
                elif ta == "이":
                    ta = "하이"
                elif ta == "정현":
                    ta = "홍"
                elif ta == "미애":
                    if fittered_data[0][0] == "장":
                        ta = "장미"
                    elif fittered_data[0][0] == "김":
                        ta = "김미"
                elif ta == "주현":
                    if fittered_data[0][0] == "오":
                        ta = "오쭈"
                    elif fittered_data[0][0] == "이":
                        ta = "이쭈"
                elif ta == "혜인":
                    if fittered_data[0][0] == "박":
                        ta = "박혜"
                    elif fittered_data[0][0] == "주":
                        ta = "주혜"
                elif ta == "지현":
                    if fittered_data[0][0] == "안":
                        ta = "안지"
                    elif fittered_data[0][0] == "정":
                        ta = "정지"
                cup = dic2[fittered_data[len(fittered_data)-2][0]]
                rec = fittered_data[len(fittered_data)-4][0:2]
                ta_and_rec(4)
                if fittered_data[len(fittered_data)-5][0:2] in dic1.keys():
                    rec = fittered_data[len(fittered_data)-5][0:2]
                    ta_and_rec(5)
                    if fittered_data[len(fittered_data)-6][0:2] in dic1.keys():
                        rec = fittered_data[len(fittered_data)-6][0:2]
                        ta_and_rec(6)
                        if fittered_data[len(fittered_data)-7][0:2] in dic1.keys():
                            rec = fittered_data[len(fittered_data)-7][0:2]
                            ta_and_rec(7)
                            if fittered_data[len(fittered_data)-8][0:2] in dic1.keys():
                                rec = fittered_data[len(fittered_data)-8][0:2]
                                ta_and_rec(8)
                                if fittered_data[len(fittered_data)-9][0:2] in dic1.keys():
                                    rec = fittered_data[len(fittered_data)-9][0:2]
                                    ta_and_rec(9)
                                    if fittered_data[len(fittered_data)-10][0:2] in dic1.keys():
                                        rec = fittered_data[len(fittered_data)-10][0:2]
                                        ta_and_rec(10)
                                        if fittered_data[len(fittered_data)-11][0:2] in dic1.keys():
                                            rec = fittered_data[len(fittered_data)-11][0:2]
                                            ta_and_rec(11)
                                            if fittered_data[len(fittered_data)-12][0:2] in dic1.keys():
                                                rec = fittered_data[len(fittered_data)-12][0:2]
                                                ta_and_rec(12)
                                                if fittered_data[len(fittered_data)-13][0:2] in dic1.keys():
                                                    rec = fittered_data[len(fittered_data)-13][0:2]
                                                    ta_and_rec(13)
                                                    # 10명까지 수용가능.
    
            
           
                        
                        
                    
   
        # 2번 알고리즘(주문하는 경우)
        elif ("부탁드립니다" in fittered_data) or ("부탁합니다" in fittered_data) or ("부탁해요" in fittered_data) or ("마십니다"in fittered_data) or ("마셔요"in fittered_data) or ("마셨어요"in fittered_data) or ("마셨습니다"in fittered_data) or ("먹어요"in fittered_data) or ("먹었어요"in fittered_data) or ("먹었습니다"in fittered_data) or ("먹습니당"in fittered_data) or ("먹어용"in fittered_data) or ("먹습니다"in fittered_data) or ("가져가요" in fittered_data) or ("가져갑니다" in fittered_data) or ("주문합니다" in fittered_data) or ("주문해요" in fittered_data) :
            menu = fittered_data[(len(fittered_data)-3)]
            cup = dic2[fittered_data[(len(fittered_data)-2)][0]]
            ta = fittered_data[0][1:3]
            # 별명으로 부르는 경우
            if ta == "루나":
                ta = "하루나"  
            elif ta == "경현":
                ta = "까루나"  
            elif ta == "이빗":
                ta = "데이빗"
            elif ta == "사님":
                ta = "목사님"
            elif ta == "모님":
                ta = "싸모님"
            elif ta == "향":
                ta = "김향"
            elif ta == "호":
                ta = "김호"
            elif ta == "설":
                ta = "정설"
            elif ta == "이":
                ta = "하이"
            elif ta == "정현":
                ta = "홍"
            elif ta == "미애":
                if fittered_data[0][0] == "장":
                    ta = "장미"
                elif fittered_data[0][0] == "김":
                    ta = "김미"   
            elif ta == "주현":
                if fittered_data[0][0] == "이":
                    ta = "이쭈"
                elif fittered_data[0][0] == "오":
                    ta = "오쭈"
            elif ta == "혜인":  
                if fittered_data[0][0] == "박":
                    ta = "박혜"
                elif fittered_data[0][0] == "주":
                    ta = "주혜"
            elif ta == "지현":
                if fittered_data[0][0] == "안":
                    ta = "안지"
                elif fittered_data[0][0] == "정":
                    ta = "정지"
            if menu[0] == "베":
                menu_def1(4000)
            elif menu[0] == "에":
                menu_def1(2500)
            elif menu[0:2] == "뜨아":
                menu_def1(2500)
            elif menu[0:2] == "따아":
                menu_def1(2500)
            elif menu[0:2] == "아아":
                menu_def1(2500)
            elif menu[0:2] == "아메":
                menu_def1(2500)
            elif menu[0] == "A":
                menu_def1(2500)
            elif menu[0] == "B":
                menu_def1(2500)
            elif menu[0] == "a":
                menu_def1(2500)
            elif menu[0] == "b":
                menu_def1(2500)
            elif menu[0:2] == "라떼":
                menu_def1(3000)
            elif menu[0:4] == "카페라떼":
                menu_def1(3000)
            elif menu[0:4] == "카푸치노":
                menu_def1(3000)
            elif menu[0:2] == "바닐":
                menu_def1(3500)
            elif menu[0:3] == "아바라":
                menu_def1(3500)
            elif menu[0:4] == "카페모카":
                menu_def1(3500)
            elif menu[0:2] == "더치":
                menu_def1(3000)
            elif menu[0:4] == "콜드브루":
                menu_def1(3000)
            elif menu[0:4] == "더치라떼":
                menu_def1(3500)
            elif menu[0:2] == "보리":
                menu_def1(2500)
            elif menu[0:3] == "탄산수":
                menu_def1(500)
            elif menu[0:2] == "우유":
                menu_def1(2000)
            elif menu[0:4] == "귀리우유":
                menu_def1(2000)
            elif menu[0:3] == "밀크티":
                menu_def1(3000)
            elif menu[0:4] == "딸기라떼":
                menu_def1(3500)
            elif menu[0:2] == "캐모":
                menu_def1(2500)
            elif menu[0:2] == "루이":
                menu_def1(2500)
            elif menu[0:2] == "보이":
                menu_def1(2500)
            elif menu[0:2] == "페퍼":
                menu_def1(2500)
            elif menu[0:3] == "레몬그":
                menu_def1(2500)
            elif menu[0:3] == "라벤더":
                menu_def1(2500)
            elif menu[0] == "차":
                menu_def1(2500)
            elif menu[0] == "티":
                menu_def1(2500)
            elif menu[0:5] == "아이스크림":
                menu_def1(2500)
            elif menu[0:2] == "맥주":
                menu_def1(3000)
            elif menu[0:2] == "무알":
                menu_def1(3000)
            elif menu[0:2] == "아바":
                menu_def1(3500)
            elif menu[0:2] == "아보":
                menu_def1(3500)
            elif menu[0:2] == "미숫":
                menu_def1(3500)
            elif menu[0:3] == "망고스":
                menu_def1(4000)
            elif menu[0:2] == "망바":
                menu_def1(4000)
            elif menu[0:3] == "망고바":
                menu_def1(4000)
            elif menu[0:2] == "아포":
                menu_def1(4000)
            elif menu[0:2] == "아인":
                menu_def1(4000)
            elif menu[0:3] == "슈페너":
                menu_def1(4000)
            elif menu[0:2] == "크림":
                menu_def1(3000)
            elif menu[0] == "브":
                menu_def1(3000)
            elif menu[0:2] == "포춘":
                menu_def1(1000)
            elif menu[0:2] == "포츈":
                menu_def1(1000)
            elif menu[0:1] == "섭":
                menu_def1()
            elif menu[0:2] == "드립":
                menu_def1()
           # 섭드립(드립), 초코, 오토밀, 샷추가 경우 추가
        
        # 3번 알고리즘(주문하는 경우)
        elif fittered_data != []:
            if (fittered_data[len(fittered_data)-1]) in ["1", "2", "3", "4", "5", "6", "7"]:
                if fittered_data[3][0:2] in dic1.keys():
                    ta = fittered_data[3][0:2]
                    if (ta == "하루") and (fittered_data[3][2] == "나"):
                        ta = "하루나"
                    elif ta == "까루":
                        ta = "까루나"
                    elif ta == "데이":
                        ta == "데이빗"
                    elif ta == "목사":
                        ta = "목사님"
                    elif ta == "대표":
                        ta = "대표님"
                    elif ta == "싸모":
                        ta = "싸모님"
                    elif ta == "데코":
                        ta = "데코팀"
                    l = 2
                    for m in range(0, (len(fittered_data)-5), 2):
                        l = l + 2
                        if fittered_data[l][0] == "베":
                            menu_def2(4000)
                        elif fittered_data[l][0] == "에":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "뜨아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "따아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "아아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "아메":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "라떼":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "카페라떼":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "카푸치노":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "바닐":
                            menu_def2(3500)
                        elif fittered_data[l][0:3] == "아바라":
                            menu_def2(3500)
                        elif fittered_data[l][0:4] == "카페모카":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "더치":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "콜드브루":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "더치라떼":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "보리":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "탄산수":
                            menu_def2(500)
                        elif fittered_data[l][0:2] == "우유":
                            menu_def2(2000)
                        elif fittered_data[l][0:4] == "귀리우유":
                            menu_def2(2000)
                        elif fittered_data[l][0:3] == "밀크티":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "딸기라떼":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "캐모":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "루이":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "보이":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "페퍼":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "레몬그":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "라벤더":
                            menu_def2(2500)
                        elif fittered_data[l][0] == "차":
                            menu_def2(2500)
                        elif fittered_data[l][0] == "티":
                            menu_def2(2500)
                        elif fittered_data[l][0:5] == "아이스크림":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "맥주":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "무알":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "아바":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "아보":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "미숫":
                            menu_def2(3500)
                        elif fittered_data[l][0:3] == "망고스":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "망바":
                            menu_def2(4000)
                        elif fittered_data[l][0:3] == "망고바":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "아포":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "아인":
                            menu_def2(4000)
                        elif fittered_data[l][0:3] == "슈페너":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "크림":
                            menu_def2(3000)
                        elif fittered_data[l][0] == "브":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "포춘":
                            menu_def2(1000)
                        elif fittered_data[l][0:2] == "포츈":
                            menu_def2(1000)
                        # 섭드립(드립), 초코, 오트밀, 샷추가 경우 추가
                        
               
                            
                # 본인이름으로 먹을떄(3-2)
                else:
                    ta = fittered_data[0][1:3]
                    if ta == "루나":
                        ta = "하루나"
                    elif ta == "이빗":
                        ta = "데이빗"
                    elif ta == "경현":
                        ta = "까루나"
                    elif ta == "사님":
                        ta = "목사님"
                    elif ta == "모님":
                        ta = "싸모님"
                    elif ta == "향":
                        ta = "김향"
                    elif ta == "호":
                        ta = "김호"
                    elif ta == "설":
                        ta = "정설"
                    elif ta == "이":
                        ta = "하이"
                    elif ta == "정현":
                        ta = "홍"
                    elif ta == "미애":
                        if fittered_data[0][0] == "장":
                            ta = "장미"
                        elif fittered_data[0][0] == "김":
                            ta = "김미"   
                    elif ta == "주현":
                        if fittered_data[0][0] == "이":
                            ta = "이쭈"
                        elif fittered_data[0][0] == "오":
                            ta = "오쭈"
                    elif ta == "혜인":  
                        if fittered_data[0][0] == "박":
                            ta = "박혜"
                        elif fittered_data[0][0] == "주":
                            ta = "주혜"
                    elif ta == "지현":
                        if fittered_data[0][0] == "안":
                            ta = "안지"
                        elif fittered_data[0][0] == "정":
                            ta = "정지"
                    l = 1
                    for m in range(0, (len(fittered_data)-3), 2):
                        l = l + 2
                        if fittered_data[l][0] == "베":
                            menu_def2(4000)
                        elif fittered_data[l][0] == "에":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "뜨아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "따아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "아아":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "아메":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "라떼":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "카페라떼":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "카푸치노":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "바닐":
                            menu_def2(3500)
                        elif fittered_data[l][0:3] == "아바라":
                            menu_def2(3500)
                        elif fittered_data[l][0:4] == "카페모카":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "더치":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "콜드브루":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "더치라떼":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "보리":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "탄산수":
                            menu_def2(500)
                        elif fittered_data[l][0:2] == "우유":
                            menu_def2(2000)
                        elif fittered_data[l][0:4] == "귀리우유":
                            menu_def2(2000)
                        elif fittered_data[l][0:3] == "밀크티":
                            menu_def2(3000)
                        elif fittered_data[l][0:4] == "딸기라떼":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "캐모":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "루이":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "보이":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "페퍼":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "레몬그":
                            menu_def2(2500)
                        elif fittered_data[l][0:3] == "라벤더":
                            menu_def2(2500)
                        elif fittered_data[l][0] == "차":
                            menu_def2(2500)
                        elif fittered_data[l][0] == "티":
                            menu_def2(2500)
                        elif fittered_data[l][0:5] == "아이스크림":
                            menu_def2(2500)
                        elif fittered_data[l][0:2] == "맥주":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "무알":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "아바":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "아보":
                            menu_def2(3500)
                        elif fittered_data[l][0:2] == "미숫":
                            menu_def2(3500)
                        elif fittered_data[l][0:3] == "망고스":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "망바":
                            menu_def2(4000)
                        elif fittered_data[l][0:3] == "망고바":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "아포":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "아인":
                            menu_def2(4000)
                        elif fittered_data[l][0:3] == "슈페너":
                            menu_def2(4000)
                        elif fittered_data[l][0:2] == "크림":
                            menu_def2(3000)
                        elif fittered_data[l][0] == "브":
                            menu_def2(3000)
                        elif fittered_data[l][0:2] == "포춘":
                            menu_def2(1000)
                        elif fittered_data[l][0:2] == "포츈":
                            menu_def2(1000)
                        # 섭드립(드립), 초코, 오트밀, 샷추가 경우 추가
                        
                            
                            
                    
                    
                                
    # 별명 추가 방법. (외자와 목사님)
    dic1["목사님"][0] = dic1["목사님"][0] + dic1["대표님"][0]
    dic1["목사님"][1] = dic1["목사님"][1] + dic1["대표님"][1]
    dic1["목사님"][2] = dic1["목사님"][2] + dic1["대표님"][2]
    dic1["목사님"][3] = dic1["목사님"][3] + dic1["대표님"][3]
    dic1["목사님"][4] = dic1["목사님"][4] + dic1["대표님"][4]
    dic1["김향"][0] = dic1["김향"][0] + dic1["향"][0] + dic1["향누"][0] + dic1["향언"][0] + dic1["향이"][0] + dic1["향님"][0] + dic1["향에"][0] + dic1["향한"][0]
    dic1["김향"][1] = dic1["김향"][1] + dic1["향"][1] + dic1["향누"][1] + dic1["향언"][1] + dic1["향이"][1] + dic1["향님"][1] + dic1["향에"][1] + dic1["향한"][1]
    dic1["김향"][2] = dic1["김향"][2] + dic1["향"][2] + dic1["향누"][2] + dic1["향언"][2] + dic1["향이"][2] + dic1["향님"][2] + dic1["향에"][2] + dic1["향한"][2]
    dic1["김향"][3] = dic1["김향"][3] + dic1["향"][3] + dic1["향누"][3] + dic1["향언"][3] + dic1["향이"][3] + dic1["향님"][3] + dic1["향에"][3] + dic1["향한"][3]
    dic1["김향"][4] = dic1["김향"][4] + dic1["향"][4] + dic1["향누"][4] + dic1["향언"][4] + dic1["향이"][4] + dic1["향님"][4] + dic1["향에"][4] + dic1["향한"][4]
    dic1["김호"][0] = dic1["김호"][0] + dic1["호"][0]+ dic1["호형"][0] + dic1["호오"][0] + dic1["호삼"][0] + dic1["호님"][0] + dic1["호에"][0] + dic1["호한"][0]
    dic1["김호"][1] = dic1["김호"][1] + dic1["호"][1] + dic1["호형"][1] + dic1["호오"][1] + dic1["호삼"][1] + dic1["호님"][1] + dic1["호에"][1] + dic1["호한"][1]
    dic1["김호"][2] = dic1["김호"][2] + dic1["호"][2]  + dic1["호형"][2] + dic1["호오"][2] + dic1["호삼"][2] + dic1["호님"][2] + dic1["호에"][2] + dic1["호한"][2]
    dic1["김호"][3] = dic1["김호"][3] + dic1["호"][3]  + dic1["호형"][3] + dic1["호오"][3] + dic1["호삼"][3] + dic1["호님"][3] + dic1["호에"][3] + dic1["호한"][3]
    dic1["김호"][4] = dic1["김호"][4] + dic1["호"][4] + dic1["호형"][4] + dic1["호오"][4] + dic1["호삼"][4] + dic1["호님"][4] + dic1["호에"][4] + dic1["호한"][4]
    dic1["정설"][0] = dic1["정설"][0] + dic1["설"][0] + dic1["설형"][0] + dic1["설오"][0] + dic1["설삼"][0] + dic1["설님"][0] + dic1["설에"][0] + dic1["설한"][0]
    dic1["정설"][1] = dic1["정설"][1] + dic1["설"][1] + dic1["설형"][1] + dic1["설오"][1] + dic1["설삼"][1] + dic1["설님"][1] + dic1["설에"][1] + dic1["설한"][1]
    dic1["정설"][2] = dic1["정설"][2] + dic1["설"][2] + dic1["설형"][2] + dic1["설오"][2] + dic1["설삼"][2] + dic1["설님"][2] + dic1["설에"][2] + dic1["설한"][2]
    dic1["정설"][3] = dic1["정설"][3] + dic1["설"][3]  + dic1["설형"][3] + dic1["설오"][3] + dic1["설삼"][3] + dic1["설님"][3] + dic1["설에"][3] + dic1["설한"][3]
    dic1["정설"][4] = dic1["정설"][4] + dic1["설"][4] + dic1["설형"][4] + dic1["설오"][4] + dic1["설삼"][4] + dic1["설님"][4] + dic1["설에"][4] + dic1["설한"][4]
    dic1["홍"][0] = dic1["홍"][0]  + dic1["홍누"][0] + dic1["홍언"][0] + dic1["홍에"][0] + dic1["홍한"][0] + dic1["홍님"][0] + dic1["홍이"][0]
    dic1["홍"][1] = dic1["홍"][1]  + dic1["홍누"][1] + dic1["홍언"][1] + dic1["홍에"][1] + dic1["홍한"][1] + dic1["홍님"][1] + dic1["홍이"][1]
    dic1["홍"][2] = dic1["홍"][2]  + dic1["홍누"][2] + dic1["홍언"][2] + dic1["홍에"][2] + dic1["홍한"][2] + dic1["홍님"][2] + dic1["홍이"][2]
    dic1["홍"][3] = dic1["홍"][3]  + dic1["홍누"][3] + dic1["홍언"][3] + dic1["홍에"][3] + dic1["홍한"][3] + dic1["홍님"][3] + dic1["홍이"][3]
    dic1["홍"][4] = dic1["홍"][4]  + dic1["홍누"][4] + dic1["홍언"][4] + dic1["홍에"][4] + dic1["홍한"][4] + dic1["홍님"][4] + dic1["홍이"][4]
    dic1["정준"][0] = dic1["정준"][0] + dic1["준이"][0] 
    dic1["정준"][1] = dic1["정준"][1] + dic1["준이"][1] 
    dic1["정준"][2] = dic1["정준"][2] + dic1["준이"][2] 
    dic1["정준"][3] = dic1["정준"][3] + dic1["준이"][3] 
    dic1["정준"][4] = dic1["정준"][4] + dic1["준이"][4] 
    dic1["지우"][0] = dic1["지우"][0] + dic1["연화"][0]
    dic1["지우"][1] = dic1["지우"][1] + dic1["연화"][1]
    dic1["지우"][2] = dic1["지우"][2] + dic1["연화"][2]
    dic1["지우"][3] = dic1["지우"][3] + dic1["연화"][3]
    dic1["지우"][4] = dic1["지우"][4] + dic1["연화"][4]
    dic1["싸모님"][0] = dic1["싸모님"][0] + dic1["싸모"][0] + dic1["사모"][0]
    dic1["싸모님"][1] = dic1["싸모님"][1] + dic1["싸모"][1] + dic1["사모"][1]
    dic1["싸모님"][2] = dic1["싸모님"][2] + dic1["싸모"][2] + dic1["사모"][2]
    dic1["싸모님"][3] = dic1["싸모님"][3] + dic1["싸모"][3] + dic1["사모"][3]
    dic1["싸모님"][4] = dic1["싸모님"][4] + dic1["싸모"][4] + dic1["사모"][4]
    
    
    
    
    
    
    del dic1["대표님"], dic1["연화"], dic1["싸모"], dic1["사모"]
    del dic1["향이"], dic1["향언"], dic1["향누"], dic1["향"], dic1["향님"], dic1["향에"], dic1["향한"]
    del dic1["호삼"], dic1["호오"], dic1["호형"], dic1["호"], dic1["호님"], dic1["호에"], dic1["호한"]
    del dic1["설삼"], dic1["설오"], dic1["설형"],  dic1["설"], dic1["설님"], dic1["설에"], dic1["설한"]
    del dic1["홍누"], dic1["홍님"], dic1["홍언"], dic1["홍에"], dic1["홍이"], dic1["홍한"]
    del dic1["준이"]
    # 나중에 다시 추가 해줘야 한다.

                       
                        
    num = 5
    for name, money in dic1.items():
        num += 1
        num = str(num)
        if money[0] > 0:
            if sheet["N"+num].value > 0:
                money1 = money[0]
                while money1 > 0:
                    if sheet["N"+num].value > 0:
                        sheet["N"+num].value -= 100
                        money1 -= 100
                    elif sheet["N"+num].value == 0:
                        sheet["F"+num].value += 100
                        money1 -= 100
            else:
                sheet["F"+num].value += money[0]
                
        if money[1] > 0:
            sheet["H"+num].value += money[1]
        
        if money[2] > 0:
            sheet["I"+num].value += money[2]
            
        if (money[1] > 0) or (money[2] > 0):
            sheet["J"+num].value += (money[1] + money[2])
        
        if money[3] > 0:
            sheet["K"+num].value += money[3]
            
        if money[4] > 0:
            sheet["N"+num].value += money[4]
        
        sheet["L"+num].value = sheet["F"+num].value
            
        num = int(num)
    
    workbook.save(file_path)
        
    
    # 한달치 정산한후에, 모든 리스트의 값을 0 으로 만들어야한다.
    
        
     
    # 행렬표를 만들기 위해, 딕셔너리형태에서 이차원리스트형태로.
    c = [["이름", "내야할돈", "먹은", "선물한", "선물받은", "남은선물"]]
    d = []
    for name, money in dic1.items():
        d.append(name)
        d.extend(money)
        c.append(d)
        d = []
    
    
    # 표를 보여준다.
    df = pd.DataFrame(c, columns=["이름", "내야할", "먹은금액", "선물한", "선물받은",  "남은선물"]) # e{at)는 먹은금액, g(vie)는 준선물, r(ecieve)은 받은선물, s(sum)는 정산결과
    print(df)
    
    # 2달을 한달(상), 한달(하)로 짤라서 서로 다른 공감.csv파일로 넣어둔다. 그다음 2달이 지난 후 최종 정산때 (상),(하) 파일을 합쳐서(폴라리오오피스로 행값을 모두 합치는 법 배우기.) 지연이모에게 최종본을 준다.
with open("doo/공감(하).csv", "w", encoding="UTF-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(c)
    
    dic1["대표님"], dic1["연화"], dic1["싸모"], dic1["사모"] = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    dic1["향이"], dic1["향언"], dic1["향누"], dic1["향"], dic1["향님"], dic1["향에"], dic1["향한"] = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    dic1["호삼"], dic1["호오"], dic1["호형"],  dic1["호"], dic1["호님"], dic1["호에"], dic1["호한"] = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    dic1["설삼"], dic1["설오"], dic1["설형"],  dic1["설"], dic1["설님"], dic1["설에"], dic1["설한"] = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    dic1["홍누"], dic1["홍님"], dic1["홍언"], dic1["홍에"], dic1["홍이"], dic1["홍한"] = [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]
    dic1["준이"] = [0, 0, 0, 0, 0]
    # 추가 !
    

print(f"1달 매출은 {sum['매출']} 입니다.")
print(df.loc[40]) # 행 정보 확인.