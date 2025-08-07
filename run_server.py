#!/usr/bin/env python
"""
Startup script for the FastAPI application with database.
"""
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import uvicorn
    from main import app
    
    print("Starting FastAPI server with database integration...")
    print("SQLite database will be created automatically.")
    print("Server will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
