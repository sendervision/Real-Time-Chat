from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    fullname: Optional[str]
    username: str
    password: str