from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_tables, save_answers

app = FastAPI()

# Enable CORS for all origins (adjust later for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB table on startup
create_tables()

@app.post("/submit_answers")
async def submit_answers(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    answers = data["answers"]
    save_answers(user_id, answers)

    return {
        "status": "received",
        "answers": [f"{item['question']} | {item['answer']}" for item in answers]
    }

@app.get("/")
def read_root():
    return {"message": "Your Conscious CEO backend is running"}

















