from mongoengine import *
from datetime import datetime
from config import d_rules, REQUEST_STATUS
# import json


class Request(Document):
    requestor_email = EmailField(required=True)
    acceptor_email = EmailField()
    title = StringField(required=True, max_length=25)
    point = PointField(required=True)  # location
    time_of_request = DateTimeField(required=True)
    request_type = StringField(required=True, choices=d_rules)
    description = StringField(required=True, max_length=280)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    # is_completed = BooleanField(
    #     default=False, required=True)  # May not need this
    status = StringField(
        required=True, choices=REQUEST_STATUS, default="POSTED")

    # There is a built-in to_json method.
    # May not need this
    # def json(self):
    #     req_dict = {
    #         "requestor_email": self.requestor_email,
    #         "acceptor_email": self.acceptor_email,
    #         "title": self.title,
    #         "location": self.point,
    #         "datetime": self.time_of_request,
    #         "category": self.request_type,
    #         "description": self.description,
    #         "time_created": self.time_created,
    #         "time_accepted": self.time_accepted,
    #         "is_completed": self.is_completed,
    #         "status": self.status
    #     }
    #     return json.dump(req_dict)

    # def __str__(self):
    #     return self.title

    # meta = {"ordering": ["-time_created"], "indexes": ["requestor_email"]}