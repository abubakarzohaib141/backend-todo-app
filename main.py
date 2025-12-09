from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import create_db_and_tables, init_db
from app.routes import auth, todo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create app
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# CORS middleware - MUST be added before routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

# Events
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Routes
app.include_router(auth.router)
app.include_router(todo.router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
