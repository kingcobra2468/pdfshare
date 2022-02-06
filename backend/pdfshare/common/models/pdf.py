from mongoengine import *


class PDF(Document):
    """PDF schematic for a given record.
    """
    title = StringField(required=True)
    fingerprint = StringField(required=True)
    cover_generated = BooleanField(required=True, default=True)
