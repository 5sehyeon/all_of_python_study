import matplotlib.pyplot as plt
import geopandas as gpd

# 세계 지도 불러오기
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 프랑크 왕국의 주요 영토를 대략적으로 지정 (현대 국가 경계 기준)
frankish_empire = world[(world.name == "France") | 
                        (world.name == "Belgium") | 
                        (world.name == "Netherlands") | 
                        (world.name == "Luxembourg") | 
                        (world.name == "Switzerland") | 
                        (world.name == "Germany") | 
                        (world.name == "Austria") | 
                        (world.name == "Italy") |
                        (world.name == "Spain")]

# 지도 그리기
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
world.boundary.plot(ax=ax, linewidth=1)
frankish_empire.boundary.plot(ax=ax, color='red', linewidth=2)
plt.title("프랑크 왕국의 영토 (8세기 후반 - 9세기 초반)")
plt.show()