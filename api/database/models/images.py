from enum import Enum

from peewee import *

from api.database import db


class Image(Model):
    """
    Image information model
    """

    class Meta:
        database = db

    class Category(Enum):
        CATGIRL = "catgirl"
        GIRL = "girl"
        KEMONOMIMI = "kemonomimi"

    file_path = CharField(primary_key=True, index=True, unique=True, max_length=500)
    category = CharField(null=True, max_length=10)
    artist = CharField(null=True, max_length=50)
    nsfw = BooleanField(default=False)
    height = IntegerField(null=True)
    width = IntegerField(null=True)

    @property
    def url(self) -> str:
        return f"https://nekos-api.tk/{self.file_path}"
