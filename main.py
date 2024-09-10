import uvicorn
from fastapi import FastAPI

from app.routers import user_routers

app = FastAPI(
    title="Avangard site"
)

app.include_router(user_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
