from database.models.user import *
from database.models.history import *
from database.models.location import *

with database:
    database.create_tables([User, Location, History])
