from pydantic import BaseModel

class User(BaseModel):
    login: str
    password: str
    name: str
    last_name: str
    age: int

    def serialize(self, exclude_password=True):
        data = self.model_dump()
        if exclude_password:
            data.pop("password", None)
        return data