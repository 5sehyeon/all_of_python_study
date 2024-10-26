# 성이 포함된 이름과, 성이 포함되지 않은 이름을 합치는 부분

lst = [("강", "은경")] # 이름들 추가,,(싸모님과 쭈이모를 어떻게 할지 고민해보자..)

dic_name = {"은경" : [7000, 4000, 3000, 0, 0], "강은경" : [9000, 3000, 6000, 0, 0]} # 예시,,


for first, second in lst:
    if (dic_name[second][4] != 0) and (dic_name[first+second][0] != 0):
        last = dic_name[first+second][0]
        while last > 0:
            if dic_name[second][4] > 0:
                dic_name[second][4] -= 100
                last -= 100
            elif dic_name[second][4] == 0:
                dic_name[second][0] += 100
                last -= 100
        dic_name[second][1] += dic_name[first+second][1]
        dic_name[second][2] += dic_name[first+second][2]
        dic_name[second][3] += dic_name[first+second][3]
        dic_name[first+second] = [0, 0, 0, 0, 0]
    
    elif (dic_name[first+second][4] != 0) and (dic_name[second][0] != 0):
        last = dic_name[second][0]
        while last > 0:
            if dic_name[first+second][4] > 0:
                dic_name[first+second][4] -= 100
                last -= 100
            elif dic_name[first+second][4] == 0:
                dic_name[first+second][0] += 100
                last -= 100
        dic_name[second][0] = dic_name[first+second][0]
        dic_name[second][4] = dic_name[first+second][4]
        dic_name[second][1] += dic_name[first+second][1]
        dic_name[second][2] += dic_name[first+second][2]
        dic_name[second][3] += dic_name[first+second][3]
        dic_name[first+second] = [0 ,0 ,0 ,0 ,0] # 성이 붙은 것은 초기화.
    
    else:
        dic_name[second][0] += dic_name[first+second][0]
        dic_name[second][1] += dic_name[first+second][1]
        dic_name[second][2] += dic_name[first+second][2]
        dic_name[second][3] += dic_name[first+second][3]
        dic_name[second][4] += dic_name[first+second][4]
        dic_name[first+second] = [0, 0, 0, 0, 0]


print(dic_name["은경"]) # "은경" 만 남기기.
print(dic_name["강은경"])