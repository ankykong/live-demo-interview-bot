from fastapi import FastAPI, HTTPException
from interview_bot import start_interview_bot

app = FastAPI()


@app.post("/start_interview")
async def start_interview():
    # Start the interview with the candidate
    # ...
    try:
        result = await start_interview_bot()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
