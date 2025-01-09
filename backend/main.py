from fastapi import FastAPI
import uvicorn
from api.endpoints import user_endpoints as users

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

if __name__ ==  "__main__":
    uvicorn.run(app, port=8000)
