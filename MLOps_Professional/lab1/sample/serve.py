import uvicorn
import logging
import warnings

from fastapi import FastAPI
from data_model import MaintenancePayload, SupportBot
from maintenance import test_maintenance


app = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")


@app.get("/ping")
async def ping():
    """Ping server to determine status

    Returns
    -------
    API response
        response from server on health status
    """
    return {"message":"Server is Running"}

@app.post("/maintenance")
async def predict(payload:MaintenancePayload):
    maintenance_result = test_maintenance(payload.temperature, payload.pressure)
    return {"msg": "Completed Analysis", "Maintenance Status": maintenance_result}

@app.post("/supportbot")
async def support(support:SupportBot):
    if support.message == "help":
        support_status = 'bring the harvester in for maintenance'
    else:
        support_status = 'No maintenance required'
    return support_status

if __name__ == "__main__":
    uvicorn.run("serve:app", host="0.0.0.0", port=5000, log_level="info")