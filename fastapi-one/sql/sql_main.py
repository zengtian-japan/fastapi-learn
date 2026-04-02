from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped,mapped_column
import  pymysql
# from sqlalchemy.testing.schema import mapped_column

print("安装完美，可以开始写代码了！")
db = create_engine("mysql+pymysql://root:zengtian@localhost/fastapi_learn",echo=True,future=True) #echo 打印 sql 语句  future 不兼容旧版本语法


class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(insert_default=func.now(),onupdate=func.now(),comment="修改时间")


if __name__ == '__main__':

    Base.metadata.create_all(db)