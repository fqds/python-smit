from models import Cargo, CargoDate



async def WriteNewCargoToDatasbase(payload: dict):
    for date in payload:
        if (await CargoDate.exists(date=date)):
            cargo_date = await CargoDate.get(date=date)
        else:
            cargo_date = await CargoDate.create(date=date)
        for cargo in payload[date]:
            await Cargo.create(
                cargo_date_id=cargo_date,
                cargo_type=cargo["cargo_type"],
                cargo_rate=cargo["rate"],
            )

async def NewCargoResponse(payload: dict):
    for date in payload:
        for cargo in payload[date]:
            cargo["cargo_price"] = _getCargoPrice(cargo_rate=cargo["rate"])
    return payload

# I can’t understand where and in what form we receive the tariff for price counting
# So i'll just leave this like here
def _getCargoPrice(cargo_rate: float):
    return cargo_rate