import numpy as np
import math

arr1 = np.array([[1,2,3,4],
                  [5,6,7,8]])

arr2 = np.array([[1,2,3,4],
                [2,2,2,2]])
print(arr1.shape) # 열 * 행
print(arr1 * 4) # 스칼라 연산(상수)
print(arr1 * arr2) # 각자 위치에 대응되는 값들 끼리 곱한다. (행렬 곱 X)
print((arr1 * arr2).sum()) # 각자 대응되는 값들을 끼리끼리 곱하고 다 더함.

arr3 = np.zeros((2,4)) # 열 * 행 의 크기를 인자로 받음
print(arr3)
arr3_1 = np.ones((2,4))
print(arr3_1) # 열 * 행의 크기를 인자로 받음

arr4 = np.arange(4)
arr4 = arr4.reshape((2,2))
print(arr4) # 1차원 배열을 2차원 배열로.

arr5 = np.array([0,1,2,3]) # 열은 달라도, 행의 갯수는 같아야한다. 
print(arr2 + arr5) # 브로드캐스팅 >>> arr5 = [[0,1,2,3],[0,1,2,3]]

# 이미지(화소)는 numpy의 배열 형태이다. np.array([]) 형태.
# R/G/B는 3차원 배열 형태이다. 3겹을 겹친것.. 색깔 O

arr6 = np.zeros((2,3,3)) # 층위(R/G/B) * 열 * 행 (3차원)  "입체구조"
# 하지만 이미지에선 열 * 행 * 층위(R/G/B) 순서이다.
print(arr6)

# 넌파이 슬라이싱 
arr7 = np.array([1, 2, 3])
arr8 = arr7[1:3] # [2,3]
arr9 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr10 = arr9[1:, 1:] # [[5,6],[8,9]] # 1st 몇 열부터 몇 열까지 선택 2nd 그 열에서, 몇 행부터 몇행까지
arr9[0:,1:3] = 8 # [[1,8,8], [4,8,8], [7,8,8]] 슬라이싱 !! 1st 열 범위 > 2nd 행 범위

# 커널 계산 (전체크기 - 커널크기 + 1)
def edge_detection(image):
    origin_c = image.shape[0]
    origin_r = image.shape[1]
    rough_result = np.zeros((origin_c - 2, origin_r - 2)) # 최종사이즈 만들고 시작
    kernal = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]]) 
    for x in range(rough_result.shape[1]):
        for y in range(rough_result.shape[0]):
            rough_result[0+y, 0+x] = (image[0+y:3+y , 0+x:3+x] * kernal).sum()
    
    result = rough_result
    
    return result

# 주변에 원그리기
def circle(img):
  column = img.shape[0]
  row = img.shape[1]
  for y in range(column):
    for x in range(row):
      if math.sqrt((x-(img.shape[1]/2))**2 + ((y-(img.shape[0]/2))**2)) > (img.shape[0]/2) :
        img[y, x] = 0
        
  result = img

  return result
