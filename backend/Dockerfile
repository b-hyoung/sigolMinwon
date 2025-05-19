# 공식 Python 이미지를 기반 이미지로 사용 (Python 3.9 안정 버전)
FROM python:3.9-slim

# 컨테이너 내부의 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치를 위해 requirements.txt를 작업 디렉토리로 복사
COPY requirements.txt ./

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 애플리케이션 코드를 작업 디렉토리로 복사
COPY . .

# 애플리케이션이 실행되는 포트 노출
EXPOSE 8000

# FastAPI 애플리케이션 실행 명령 정의
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]