from fastapi import FastAPI

app = FastAPI(title="Inventory API")


@app.get("/health")
def health():
    return {"service": "inventory-api", "status": "ok"}


@app.get("/inventory")
def inventory():
    return [{"sku": "DEMO-001", "available": 10}]
