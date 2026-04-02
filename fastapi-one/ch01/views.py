from datetime import date
from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator


class Address(BaseModel):
    province: str
    city: str
    county: str

class enum_names(Enum):
    one = "zt"
    two = "zengtian"
    three = "tian"
class Emp(BaseModel):
    name: str = Field(description="员工的名字")
    age: int = Field(description="员工的年龄")
    birthday: date = Field(description="员工的出生日期",default = None)
    address: Address = Field(description="员工的地址")
    @field_validator("name")
    def validate_name(cls, value):
        if value not in [ item.value for item in enum_names ]:
            raise ValueError(f'名字必须是 {list(enum_names)} 中的一个')
        return value

router = APIRouter(prefix="/ch01", tags=["请求体传参"])


@router.post("/", response_model=Emp)
async def find_add_emp(emp: Emp):
    return emp

