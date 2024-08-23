from api.auth import auth_routes
from api.user import user_routes
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "status": "ok",
        "version": "0.0.1",
        "documentation": "/docs",
    }


app.include_router(auth_routes.router)
app.include_router(user_routes.router)
