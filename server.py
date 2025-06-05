import os
from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Начальные значения метрик
metrics = {
    "weight": 81,
    "sleep": 7.5,
    "steps": 11738,
    "recommendation": "Изучив ваши данные, могу порекомендовать уделить внимание качеству отдыха — 7.5 часов сна это хорошо, но для максимального восстановления энергии попробуйте иногда увеличивать продолжительность сна до 8 часов и поддерживать регулярную физическую активность."
}

@app.get("/api/metrics")
async def get_metrics():
    return metrics

@app.post("/api/webhook")
async def webhook(request: Request, x_webhook_secret: str = Header(...)):
    secret = os.getenv("WEBHOOK_SECRET")
    if not secret or x_webhook_secret != secret:
        raise HTTPException(status_code=403, detail="Invalid webhook secret")
    data = await request.json()
    for key in metrics:
        if key in data:
            metrics[key] = data[key]
    return JSONResponse(content={"status": "ok", "metrics": metrics})
