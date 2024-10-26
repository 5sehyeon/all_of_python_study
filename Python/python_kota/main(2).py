import os

# 폴더 경로 지정
folder_path = "C:/Users/djdjd/OneDrive/바탕 화면/카카오톡다운로드"  # 변경할 경로 입력

# 폴더 내 파일 목록 가져오기
files = os.listdir(folder_path)
print(files)

# 파일 목록을 생성일자 기준으로 정렬
files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

# 파일 이름 일괄 변경
for i, filename in enumerate(files):
    # 확장자 분리
    file_extension = os.path.splitext(filename)[1]
    # 새 이름 생성 (예: photo(1).jpg)
    new_name = f"photo({i + 1}){file_extension}"
    # 파일 이름 변경
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

print("이름 변경 완료!")





