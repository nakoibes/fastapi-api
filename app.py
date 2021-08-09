from fastapi import FastAPI

from core.routes import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def index():
    return "Чтобы ознакомиться с документацией, перейдите на /docs"
