from dataclasses import dataclass


@dataclass
class ValuteRange:
    id: str
    num_code: int
    char_code: str
    nominal: int
    name: str
    min: float
    max: float


@dataclass
class ValutesConfig:
    valutes: list[ValuteRange]
