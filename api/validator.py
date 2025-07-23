from dataclasses import dataclass
from datetime import datetime


@dataclass
class Validator:
    # True - дата прошла валидацию, False - не прошла
    @staticmethod
    async def validate_date(date_req: str) -> bool:
        date_format = ("%d/%m/%Y", "%d.%m.%Y")
        for df in date_format:
            try:
                datetime.strptime(date_req, df)
                return True
            except ValueError:
                continue
        return False
