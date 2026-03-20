from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ===== INPUT STRUCTURE =====
class TradeRequest(BaseModel):
    symbol: str
    qty: int
    side: str   # BUY / SELL
    sl: float

# ===== HEALTH CHECK =====
@app.get("/")
def home():
    return {"status": "running"}

# ===== TRADE API =====
@app.post("/trade")
def trade(data: TradeRequest):

    print("TRADE RECEIVED:", data)

    return {
        "status": "executed",
        "symbol": data.symbol,
        "side": data.side,
        "qty": data.qty,
        "sl": data.sl
    }
