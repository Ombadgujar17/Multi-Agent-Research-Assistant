from fastapi import FastAPI

app = FastAPI(title="Multi-Agent Research Assistant")

@app.get("/")
def root():
    return {"message": "Multi-Agent Research Assistant is running!"}