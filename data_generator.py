# https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002
import json
import httpx
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


# @dataclass
# class Valute:
#     id = "R01010"
#     num_code: int
#     char_code: str
#     nominal: int
#     name: str
#     value: float
#     vunit_rate: float


def data_generator(start_date: str, end_date: str) -> None:
    start_dt = datetime.strptime(start_date, "%d/%m/%Y")
    end_dt = datetime.strptime(end_date, "%d/%m/%Y")
    current_date = start_dt
    data = {}
    while current_date <= end_dt:

        response = httpx.get(
            url=f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date.day:02d}/{current_date.month:02d}/{current_date.year}"
        )

        current_date += timedelta(days=1)
        soup = BeautifulSoup(response.text, "xml")
        valutes = soup.find_all("Valute")

        for valute in valutes:
            valute_id = valute["ID"]
            valute_data = data.get(valute_id)
            value = float(valute.Value.text.replace(",", "."))

            if valute_data:
                if data[valute_id]["min"] is None or value < data[valute_id]["min"]:
                    data[valute_id]["min"] = value
                    data[valute_id]["last_value"] = value

                if data[valute_id]["max"] is None or value > data[valute_id]["max"]:
                    data[valute_id]["max"] = value
                    data[valute_id]["last_value"] = value
            else:
                data[valute_id] = {
                    "id": valute_id,
                    "num_code": valute.NumCode.text,
                    "char_code": valute.CharCode.text,
                    "nominal": int(valute.Nominal.text),
                    "name": valute.Name.text,
                    "min": None,
                    "max": None,
                    "vunit_rate": valute.VunitRate.text,
                    "first_value": value,
                    "last_value": None,
                }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
