from mongoengine import *


class PDF(Document):
    title = StringField(required=True)
    fingerprint = StringField(required=True)
    cover_generated = BooleanField(required=True, default=True)
