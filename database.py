
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:0000@127.0.0.1:3306/todoapplicationdatabase'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:KhCnBptVm9NAkPG5@db.epxhvtexuhopitruwszi.supabase.co:5432/postgres'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres.epxhvtexuhopitruwszi:KhCnBptVm9NAkPG5@aws-1-eu-west-1.pooler.supabase.com:6543/postgres'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

