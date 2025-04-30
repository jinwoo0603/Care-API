from enum import Enum

class MEASUREMENT_TYPE(Enum):
    BLOOD_SUGAR = "blood_sugar"
    BLOOD_PRESSURE = "blood_pressure"
    WEIGHT = "weight"

class RESULT_CODE(Enum):
    SUCCESS = 1
    NOT_FOUND = -2
    FAILED = -3
