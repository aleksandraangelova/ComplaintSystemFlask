from marshmallow import fields
from marshmallow_enum import EnumField

from models import ComplaintState
from schemas.base import ComplaintBase


class ComplaintSchemaResponse(ComplaintBase):
    id = fields.Int(required=True)
    created_on = fields.DateTime()
    status = EnumField(ComplaintState, by_value=True)
    photo_url = fields.String(required=True)
    # TODO: make nested schema for complainer obj
    # complainer = fields.Nested()

