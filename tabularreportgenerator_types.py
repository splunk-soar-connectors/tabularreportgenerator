import abc
# from typing_extensions import Protocol
from typing import List, Union

from pydantic import BaseModel, Field


class Row(BaseModel, abc.ABC):
    type: str


class KVRow(BaseModel):
    key: str
    value: str
    type: str = Field(default="kv_row")


class HeadingRow(BaseModel):
    value: str
    type: str = Field(default="heading_row")


class TextRow(BaseModel):
    value: str
    type: str = Field(default="text_row")


class LRRow(BaseModel):
    left: str
    right: str
    type: str = Field(default="lr_row")


class ImageRow(BaseModel):
    cid: str
    type: str = Field(default="image_row")


class Report(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    message: str
    rows: List[Union[KVRow, HeadingRow, TextRow, ImageRow, LRRow]]
