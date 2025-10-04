from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url='mysql+pymysql://root:1234@localhost:3306/education'
engine=create_engine(db_url,echo=True)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
