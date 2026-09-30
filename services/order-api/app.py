from fastapi import FastAPI

app = FastAPI(title="Order API")


@app.get("/health")
def health():
    return {"service": "order-api", "status": "ok"}


@app.get("/orders")
def orders():
    return [{"id": 1, "status": "created"}]
