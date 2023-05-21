from pydantic import BaseModel, Extra
from pathlib import Path


class Config(BaseModel, extra=Extra.ignore):
    WORKDIR = Path('data/rp').absolute()
    DATABASE_PATH = WORKDIR / 'db.json'
