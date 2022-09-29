import dataclasses
import datetime
from typing import List


from .unit import Unit, ServiceCharges

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class SeatMapOD(FromDictMixin):
    arrival_station: str = None
    departure_station: str = None
    available_units: int = None
    seatmap_reference: str = None
    units: List[Unit] = dataclasses.field(default_factory=list)

    @staticmethod
    def get_units(units, fees_json):
        unit_array = []
        for unit in units:
            if unit['unitKey'] != None:
                fees = []
                for key, value in fees_json.items():
                    for fee in value['groups'][str(unit['group'])]['fees']:
                        serviceCharges = []
                        for service in fee['serviceCharges']: serviceCharges.append(ServiceCharges.from_dict(service))
                        fees.append({
                            "passengerKey": key,
                            "serviceCharges": serviceCharges
                        })
                unit['fees'] = fees
                unit['row'] = int(unit['designator'][:-1])
                unit['column'] = unit['designator'][-1]
                unit_array.append(Unit.from_dict(unit))
        return unit_array

    @classmethod
    def from_dict(cls, obj):
        # price_obj = list(obj['pricesByJourney'].values())[0]
        seatMap = obj['seatMap']
        fees = obj['fees']
        return cls(
            arrival_station = seatMap['arrivalStation'],
            departure_station = seatMap['departureStation'],
            available_units = seatMap['availableUnits'],
            seatmap_reference = seatMap['seatmapReference'],
            units = cls.get_units(seatMap["decks"]["1"]["compartments"]["Y"]["units"], fees)
        )


@dataclasses.dataclass
class SeatMap(FromDictMixin):
    seat_maps: List[SeatMapOD]

    @classmethod
    def from_dict(cls, obj):
        # price_obj = list(obj['pricesByJourney'].values())[0]
        # print(obj)
        # print(seatMap["decks"]["1"]["compartments"]["Y"]["units"][0])
        return cls(
            seat_maps = [SeatMapOD.from_dict(seat_map) for seat_map in obj]
        )

    def normalize_coordinates(self):
        x_min = min(unit.x for seat_map in self.seat_maps for unit in seat_map.units)
        y_min = min(unit.y for seat_map in self.seat_maps for unit in seat_map.units)
        for seat_map in self.seat_maps:
            for unit in seat_map.units:
                unit.x -= x_min
                unit.y -= y_min