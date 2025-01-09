from pydantic import BaseModel

class User(BaseModel):
    login: str
    password: str
    name: str
    last_name: str
    age: int

    def serialize(self):
        data = self.model_dump()
        return data