from pydantic import BaseModel

class Customers_class(BaseModel):
    firstname: str
    lastname: str
    email: str
    phonenumber: str
    date: str


class Complain_Classes(BaseModel):
    firstname: str
    email: str
    date: str
    complain: str