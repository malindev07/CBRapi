import json

from config_model import ValuteRange


async def load_data() -> list[ValuteRange]:
    try:
        with open("config/config.json", "r", encoding="utf-8") as f:
            data = []
            json_data = json.load(f)
            for key in json_data:

                data.append(
                    ValuteRange(
                        id=json_data[key]["id"],
                        num_code=json_data[key]["num_code"],
                        char_code=json_data[key]["char_code"],
                        nominal=json_data[key]["nominal"],
                        name=json_data[key]["name"],
                        min=json_data[key]["min"],
                        max=json_data[key]["max"],
                    )
                )
            return data
    except FileNotFoundError:
        raise FileNotFoundError()
