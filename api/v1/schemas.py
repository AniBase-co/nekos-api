import typing

from pydantic import BaseModel
from pydantic.utils import GetterDict

import peewee

from api.database.models.images import Image


class PeeweeGetterDict(GetterDict):
    def get(self, key: typing.Any, default: typing.Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class Image(BaseModel):
    url: str
    artist: typing.Optional[str]
    category: Image.Category
    nsfw: bool

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ImageList(BaseModel):
    images: typing.List[Image]