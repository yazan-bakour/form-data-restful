from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.form_data_routes import router as form_data_router
from database import create_tables
import os
from dotenv import load_dotenv
from database.connection import engine
from database.models import Base

load_dotenv()

API_TITLE = os.getenv("API_TITLE", "My API Server")
API_VERSION = os.getenv("API_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for FastAPI application.
    Handles startup and shutdown events.
    """
    
    print("🚀 Starting up the application...")
    
    Base.metadata.create_all(bind=engine)
    print("📊 Database tables created successfully!")
    
    yield
    
    print("🛑 Shutting down the application...")

app = FastAPI(
    title=API_TITLE, 
    version=API_VERSION,
    description="A REST API for handling form data with FastAPI and PostgreSQL/SQLite",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=DEBUG,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form_data_router)

@app.get("/")
def read_root():
    return {
        "message": "Hello World", 
        "status": "API Server is running!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
