from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    REPEAT_COUNT = 2
    MAX_SAMPLES = 10
