import sqlite3

# 데이터베이스 및 테이블 생성
def create_database():
    conn = sqlite3.connect('medicine_app.db')
    cursor = conn.cursor()

    # 질병 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    ''')

    # 약 테이블 생성
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        side_effects TEXT,
        disease_id INTEGER,
        FOREIGN KEY(disease_id) REFERENCES diseases(id)
    )
    ''')

    conn.commit()
    conn.close()

# 질병 정보 삽입
def insert_disease(name, description):
    conn = sqlite3.connect('medicine_app.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO diseases (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()

# 약 정보 삽입
def insert_medication(name, description, side_effects, disease_id):
    conn = sqlite3.connect('medicine_app.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO medications (name, description, side_effects, disease_id) VALUES (?, ?, ?, ?)', (name, description, side_effects, disease_id))
    conn.commit()
    conn.close()

# 질병에 맞는 약 찾기
def get_medications_for_disease(disease_name):
    conn = sqlite3.connect('medicine_app.db')
    cursor = conn.cursor()

    # 질병 이름으로 질병 ID 가져오기
    cursor.execute('SELECT id FROM diseases WHERE name = ?', (disease_name,))
    disease = cursor.fetchone()

    if disease:
        disease_id = disease[0]
        # 질병 ID로 관련된 약 조회
        cursor.execute('SELECT name, description, side_effects FROM medications WHERE disease_id = ?', (disease_id,))
        medications = cursor.fetchall()
    else:
        medications = []

    conn.close()
    return medications

# 데이터베이스 초기화
create_database()

# 예시 데이터 삽입
insert_disease("감기", "일반적인 감기 증상")
insert_disease("두통", "머리의 통증을 유발하는 질환")

insert_medication("타이레놀", "통증과 열을 줄이는 데 사용", "간 손상 위험", 2)  # 두통과 관련
insert_medication("판피린", "감기 증상 완화", "졸음 유발", 1)  # 감기와 관련

# 질병에 맞는 약 정보 조회
disease_name = "두통"  # 사용자가 입력한 질병 이름
medications = get_medications_for_disease(disease_name)

# 결과 출력
if medications:
    for med in medications:
        print(f"약 이름: {med[0]}, 설명: {med[1]}, 부작용: {med[2]}")
else:
    print("해당 질병에 맞는 약이 없습니다.")
