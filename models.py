from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class CargoDate(models.Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(unique=True)

class Cargo(models.Model):
    id = fields.IntField(pk=True)
    cargo_date_id = fields.ForeignKeyField(model_name="models.CargoDate",on_delete="CASCADE")
    cargo_type = fields.CharField(max_length=20)
    cargo_rate = fields.FloatField()


CargoDate_Pydantic = pydantic_model_creator(CargoDate, name="cargo_date")
CargoDate_Pydantic = pydantic_model_creator(Cargo, name="cargo")
# UserIn_Pydantic = pydantic_model_creator(CargoDate, name="UserIn", exclude_readonly=True)