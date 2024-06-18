from app.models.statistic import Statistic
from marshmallow import fields, Schema, post_load

class StatisticSchema(Schema):
    id = fields.Integer(dump_only=True)
    events_participated = fields.String(required=True)
    wins = fields.String(required=True)
    losses = fields.String(required=True)
    goals_scored = fields.String(load_only=True)
    assists = fields.String(load_only=True)
    heights = fields.String(load_only=True)
    weight = fields.String(load_only=True)
    data = fields.Dict(required=False)

    @post_load
    def make_statistic(self, data, **kwargs):
        return Statistic(**data)