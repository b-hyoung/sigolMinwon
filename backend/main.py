from fastapi import FastAPI
from sqlalchemy import create_engine
import settings

app = FastAPI()

DATABASE_URL = (
    f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}"
    f"@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"
)

engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT VERSION()")
            version = result.fetchone()
        return {"message": f"MySQL 연결 성공! 버전: {version[0]}"}
    except Exception as e:
        return {"error": str(e)}