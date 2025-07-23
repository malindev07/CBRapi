from dataclasses import dataclass


@dataclass
class Valute:
    id: str
    num_code: int
    char_code: str
    nominal: int
    name: str
    value: float
    vunit_rate: float
