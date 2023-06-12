from database.models.base import *
from datetime import datetime


class User(BaseModel):
    user_id = IntegerField(unique=True)
    timestamp = DateTimeField(default=datetime.now)
    command = TextField(null=True)
    region_id = CharField(null=True)
    city = TextField(null=True)
    location = CharField(null=True)
    date_in = DateField(null=True)
    date_out = DateField(null=True)
    hotels_num = IntegerField(null=True)
    photo_num = IntegerField(default=0)
    min_price = IntegerField(default=10)
    max_price = IntegerField(default=200)
    distance = IntegerField(default=0)

    class Meta:
        db_table = 'Users'
