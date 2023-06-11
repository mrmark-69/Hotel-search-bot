from database.models.history import History


def make_history(user):
    History.create(user_id=user.user_id, command=user.command, location=user.location,
                   city=user.city)
    History.delete().where((History.user_id == user.user_id) & (History.id.not_in(
        History.select(History.id).where(History.user_id == user.user_id).order_by(History.timestamp.desc()).limit(10)
    ))).execute()
