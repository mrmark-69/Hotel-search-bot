from database.SQLite_database import *


class BaseModel(Model):
    class Meta:
        database = database
        order_by = id
