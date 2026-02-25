from enum import Enum

class MOOD_METHOD(Enum):
        SET = "SET"
        CALCULATE = "CALCULATE"
    
class MOOD(Enum):
    HAPPY = "HAPPY"
    SAD = "SAD"
    ANGRY = "ANGRY"

class SEX(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"