import sqlite3
import streamlit as st

import sqlite3

# DB 연결 함수
def connect_job_seekers_db():
    db_path = 'job_seekers.db'  # DB 파일 경로
    conn = sqlite3.connect(db_path)
    return conn

# 구직자 정보를 저장할 테이블 생성
def create_job_seekers_table():
    conn = connect_job_seekers_db()
    cursor = conn.cursor()

    # job_seekers 테이블 생성 (빈 테이블)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_seekers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            disability TEXT,
            severity TEXT
        )
    ''')

    conn.commit()
    conn.close()

# 테이블 생성
create_job_seekers_table()

# 구직자 정보를 DB에 저장하는 함수
def save_job_seeker(name, disability, severity):
    conn = connect_job_seekers_db()  # DB 연결
    cursor = conn.cursor()
    
    # 구직자 정보 'job_seekers' 테이블에 저장
    cursor.execute("INSERT INTO job_seekers (name, disability, severity) VALUES (?, ?, ?)", (name, disability, severity))
    
    conn.commit()  # 변경 사항 커밋
    conn.close()   # DB 연결 종료

# 테이블 구조 확인 함수
def check_job_seekers_table():
    conn = connect_job_seekers_db()
    cursor = conn.cursor()

    # 'job_seekers' 테이블의 구조 확인
    cursor.execute("PRAGMA table_info(job_seekers);")
    columns = cursor.fetchall()
    print("job_seekers 테이블 컬럼:")
    for column in columns:
        print(column)

    conn.close()

# 테이블 생성 및 확인
create_job_seekers_table()  # 테이블 생성
check_job_seekers_table()   # 테이블 구조 확인

# Streamlit UI 예시
st.title("장애인 일자리 매칭 시스템")

role = st.selectbox("사용자 역할 선택", ["구직자", "구인자"])

if role == "구직자":
    name = st.text_input("이름 입력")
    disability = st.selectbox("장애유형", ["시각장애", "청각장애", "지체장애", "뇌병변장애", "언어장애", "안면장애", "신장장애", "심장장애", "간장애", "호흡기장애", "장루·요루장애", "뇌전증장애", "지적장애", "자폐성장애", "정신장애"])
    severity = st.selectbox("장애 정도", ["심하지 않은", "심한"])
    
    if st.button("매칭 결과 보기"):
        # 구직자 정보 저장
        save_job_seeker(name, disability, severity)
        
        st.write(f"구직자 정보가 저장되었습니다: {name}, {disability}, {severity}")

elif role == "구인자":
    job_title = st.text_input("일자리 제목 입력")
    abilities = st.multiselect("필요한 능력 선택", ["주의력", "아이디어 발상 및 논리적 사고", "기억력", "지각능력", "수리능력", "공간능력", "언어능력", "지구력", "유연성 · 균형 및 조정", "체력", "움직임 통제능력", "정밀한 조작능력", "반응시간 및 속도", "청각 및 언어능력", "시각능력"])
    
    if st.button("매칭 결과 보기"):
        # 구인자 정보 저장
        save_job_posting(job_title, abilities)
        st.success("구인자 정보가 저장되었습니다!")
        st.write("일자리 제목:", job_title)
        st.write("필요 능력:", ", ".join(abilities))  # 능력 리스트를 쉼표로 구분해서 표시

# 유료 서비스 여부 확인
if st.button("대화 종료"):
    if role == "구직자":
        use_service = st.radio("유료 취업준비 서비스 이용하시겠습니까?", ["네", "아니요"])
    else:
        use_service = st.radio("유료 직무개발 서비스 이용하시겠습니까?", ["네", "아니요"])
    if use_service == "네":
        st.write("서비스를 이용해 주셔서 감사합니다!")
    else:
        st.write("대화를 종료합니다.")
