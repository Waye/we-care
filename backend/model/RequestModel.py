from mongoengine import *
from datetime import datetime
from backend.config import *
from backend.model.UserModel import User
from backend.model.UserModel import Preferences

# todo: add default values and data length restrictions

class Request(Document):
    request_id = IntField(unique=True, required=True)
    requester_user = ReferenceField(User, required=True)
    request_location = PointField()
    request_time = DateField(default=datetime.utcnow)  # may be a date in the future
    preferences = EmbeddedDocumentField(Preferences, required=True)
    description = StringField(required=True)  # todo add limit
    time_created = DateField(required=True, default=datetime.utcnow)
    is_complete = BooleanField(required=True, default=False)  # set to True when another user accept the request or

    meta = {
        "indexes": ["request_id"],
        "ordering": ["-is_complete", "request_id"]
    }
    userId = StringField(required=True)

class AcceptRequest(Document):
    # Note some requests may never be accepted
    request_id = IntField(unique=True, required=True)
    acceptor_user = ReferenceField(User, required=True)
    time_accepted = DateField(required=True, default=datetime.utcnow)
    userId = StringField(required=True)