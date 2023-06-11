from peewee import *
from database.models.base import *
from datetime import datetime
# from database.models.user import *


class History(BaseModel):
    user_id = IntegerField(null=True)
    timestamp = DateTimeField(default=datetime.now)
    command = TextField(null=True)
    location = CharField(null=True)
    city = TextField(null=True)

    class Meta:
        db_table = 'History'
