"""
Exam Bank System - Main Application
A simple exam bank management system built with FastAPI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Exam Bank System",
    description="API for managing exam questions and test banks",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "status": "healthy",
        "message": "Welcome to Exam Bank System API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run"""
    return {"status": "ok"}


@app.get("/api/v1/exams")
async def list_exams():
    """List all exams - placeholder endpoint"""
    return {
        "exams": [],
        "total": 0,
        "message": "This is a placeholder endpoint. Implement your exam logic here."
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
