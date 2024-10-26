import gspread
from google.oauth2.service_account import Credentials
from gspread_formatting import *
from googleapiclient.discovery import build

# 자격 증명 파일 경로 (다운로드한 JSON 파일의 경로를 입력하세요)
creds_path = "C:/Users/djdjd/Downloads/sanguine-sign-436506-k7-ccbb794af6c1.json"

# 구글 스프레드시트와 드라이브 접근을 위한 권한 범위 설정
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# 자격 증명 로드
credentials = Credentials.from_service_account_file(creds_path, scopes=SCOPES)

# gspread 클라이언트 생성
client = gspread.authorize(credentials)

# 스프레드시트 ID로 연결 (스프레드시트 URL에서 ID를 가져옵니다)
spreadsheet_id = '1deFHEu9KodtwjTMKc3Fez5lSIy_VWBakJwk-lJgKuZE' # 내 구글 시트 링크.
spreadsheet = client.open_by_key(spreadsheet_id)

# 첫 번째 워크시트 선택
sheet = spreadsheet.get_worksheet(0)

# cell에 텍스트값 업로드
sheet.update_cell(3,3,"HELLO")

# 셀 꾸미기
fmt = CellFormat(backgroundColor=Color(1,0.75,0.8), # 배경색
                 textFormat=TextFormat(bold=True))  # 글씨굵기
format_cell_range(sheet, 'C3', fmt) # 주소는 '영어+숫자' 형식으로 적어야 한다.

# 셀에 사진 박기
image_url = "https://drive.google.com/uc?id=1pRG-dl-dYVGMdrwAAwcU3Sf6eB_UO6WU"

sheet.update_cell(1,1,f'=IMAGE("{image_url}")')

drive_service = build('drive', 'v3', credentials=credentials)

# 폴더 ID와 이미지 파일 가져오기
folder_id = '1CSjt_1nRMZrguO_06RVs4zeBQRt4l8yp'  # 구글 드라이브 폴더 ID를 입력하세요
query = f"'{folder_id}' in parents and (mimeType='image/jpeg' or mimeType='image/png')"  # JPEG 및 PNG 이미지 쿼리
results = drive_service.files().list(q=query, fields="files(id, name)").execute()
items = results.get('files', [])

# 이미지 URL 생성 및 구글 스프레드시트에 삽입
for index, item in enumerate(items):
    image_url = f"https://drive.google.com/uc?id={item['id']}"
    image_formula = f'=IMAGE("{image_url}")'
    sheet.update_cell(index + 4, 1, image_formula)




