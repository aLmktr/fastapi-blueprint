from api.auth import auth_routes
from api.user import user_routes
from fastapi import FastAPI

app = FastAPI()


app.include_router(auth_routes.router)
app.include_router(user_routes.router)
