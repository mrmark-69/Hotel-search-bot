from peewee import *
from database.models.base import *


class Location(BaseModel):
    user_id = IntegerField(null=True)
    region_id = IntegerField(null=True)
    location_name = CharField(null=True)

    class Meta:
        db_table = 'locations'
