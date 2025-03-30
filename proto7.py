import sqlite3

# DB 연결 함수 (정확한 경로로 연결)
def connect_db():
    db_path = '/mnt/data/job_seekers.db'  # DB 파일 경로
    conn = sqlite3.connect(db_path)  # DB 파일 경로로 연결
    return conn

# 구직자 정보를 DB에 저장하는 함수
def save_job_seeker(name, disability, severity):
    conn = connect_db()  # DB 연결
    cursor = conn.cursor()
    
    # 구직자 정보 'job_seekers' 테이블에 저장
    cursor.execute("INSERT INTO job_seekers (name, disability, severity) VALUES (?, ?, ?)", (name, disability, severity))
    
    conn.commit()  # 변경 사항 커밋
    conn.close()   # DB 연결 종료

# 예시 사용법
name = "홍길동"
disability = "시각장애"
severity = "심한"

# 구직자 정보 저장
save_job_seeker(name, disability, severity)
