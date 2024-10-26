import pandas as pd
import geopandas
import matplotlib.pyplot as plt
# geopandas dataframe 객체 생성
countries = geopandas.read_file('data/ne_110m_admin_0_countries.shp') 
# 기본 지도 생성
countries.plot(figsize=(15, 7))
#1st 색칠할 나라 특정하기,,
#2nd 특정한 나라.plot()을 하면, 해당 나라가 통일된 색깔로 색칠된다.
#3rd 어떤 기준에 따라, 색깔을 다르게 칠하고 싶다면 .plot(column=@, legned=True) 옵션을 넣는다.
# 열@ 이 나라마다 색깔을 달리 칠하게되는 기준이 된다.
#4rd 특정나라.plot(column=@,legend=True),,,특정나라[@]과 특정나라의 열의 수가 같아야한다.
# (각 나라마다 해당국가[@]이 1대1 매칭되어 색깔이 그에 따라 다르게 색칠 !!)
south_america = countries[countries['CONTINENT'] == 'South America'] # 남미로 특정.
south_america.plot(column='POP_EST', legend=True, figsize=(15, 7))
print(south_america.shape)
print(south_america["POP_EST"])
# 각각의 두 나라를 하나의 그래프위에 색칠하고 싶다면,,,,fig,ax = plt.subplots(),,,,(ax=ax) 옵션!!
fig , ax = plt.subplots(figsize=(15,7))
small_country = countries[(countries["GDP_MD_EST"] > 500000) & (countries["POP_EST"] < 80000000)] # 나라 특정.
rich_and_small = (countries.loc[(countries["GDP_MD_EST"] > 500000) & (countries["POP_EST"] < 80000000), "GDP_MD_EST"])
else_country = countries[(countries["GDP_MD_EST"] < 500000) | (countries["POP_EST"] > 80000000)] # 나라 특정.
poor_and_big = (countries.loc[(countries["GDP_MD_EST"] < 500000) | (countries["POP_EST"] > 80000000), "GDP_MD_EST"])
small_country.plot(ax=ax, column=rich_and_small, legend=True )
else_country.plot(ax=ax, column=poor_and_big, color="gray") # 하나의 그래프 위에......
# else_country와 small_country는 여집합 관계!! &은 and 연산 |은 or 연산.
    

