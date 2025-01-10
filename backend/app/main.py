from fastapi import FastAPI
import uvicorn
from api.endpoints import user_endpoints as users, auth_endpoints as auth, role_endpoints as roles

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(roles.router, prefix="/api/v1/roles", tags=["Roles"])

if __name__ ==  "__main__":
    uvicorn.run(app, port=8000)
