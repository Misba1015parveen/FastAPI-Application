from fastapi import FastAPI

app = FastAPI(
    title="DevOps Assignment API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the DevOps Assignment"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }