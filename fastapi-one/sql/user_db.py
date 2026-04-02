from sql_main import Base,db
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import String, Column, Integer,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True,comment="用户id")
    name: Mapped[str] = mapped_column(String(40),unique=True,nullable=False)
    age: Mapped[int] = mapped_column(Integer,nullable=False)
    gender: Mapped[int] = mapped_column(Integer,nullable=False)


if __name__ == '__main__':

    Base.metadata.create_all(db)