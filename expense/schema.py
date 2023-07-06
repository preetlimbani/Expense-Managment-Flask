from expense import ma
from marshmallow import fields


class ExpenseSchema(ma.Schema):
    id = fields.Str(data_key='_id')
    amount = fields.Float()
    title = fields.Str()
    description = fields.Str()