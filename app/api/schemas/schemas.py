from pydantic import BaseModel

from app.config import my_enum

class MoveRequest(BaseModel):
    entity_id: int
    target_x: int
    target_y: int

class CreateNpcRequest(BaseModel):
    name: str
    x: int
    y: int

class EatRequest(BaseModel):
    entity: int
    value: int

class SetMoodRequest(BaseModel):
    entity: int
    mood:my_enum.MOOD
    value: float
    method:my_enum.MOOD_METHOD

