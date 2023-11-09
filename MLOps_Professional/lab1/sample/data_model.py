from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int
    pressure: int

class SupportBot(BaseModel):
    message: str