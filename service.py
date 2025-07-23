import asyncio
import json
import random
from dataclasses import dataclass
from xml.etree import ElementTree as et

from valute_model import Valute, ValuteRange


@dataclass
class Service:

    # Выборка валют из БД
    @staticmethod
    async def get_random_valutes_count(valutes: list[ValuteRange]) -> list[Valute]:
        with open("data.json", "r", encoding="utf-8") as f:
            l = len(valutes)

            rand_count = random.randint(1, l)

            data = []
            for valute in range(rand_count):
                value = round(
                    random.uniform(
                        float(valutes[valute].min),
                        float(
                            valutes[valute].max,
                        ),
                    ),
                    4,
                )
                vunit_rate = round(value / valutes[valute].nominal, 4)
                data.append(
                    Valute(
                        id=valutes[valute].id,
                        num_code=valutes[valute].num_code,
                        char_code=valutes[valute].char_code,
                        nominal=valutes[valute].nominal,
                        name=valutes[valute].name,
                        value=value,
                        vunit_rate=vunit_rate,
                    )
                )

            return data

    # Форма XML c рандомно сгенерированными данными
    async def get_xml_data(self, date_req: str, valutes: list[ValuteRange]) -> str:
        valutes = await self.get_random_valutes_count(valutes)
        xml_str = ""
        elem = et.Element("ValCurs")
        elem.set("Date", date_req)
        elem.set("name", "Foreign Currency Market")

        for valute in valutes:

            valute_elem = et.SubElement(elem, "Valute")
            valute_elem.set("ID", valute.id)

            et.SubElement(valute_elem, "NumCode").text = str(valute.num_code)
            et.SubElement(valute_elem, "CharCode").text = valute.char_code
            et.SubElement(valute_elem, "Nominal").text = str(valute.nominal)
            et.SubElement(valute_elem, "Name").text = valute.name
            et.SubElement(valute_elem, "Value").text = str(valute.value).replace(
                ".", ","
            )
            et.SubElement(valute_elem, "VunitRate").text = str(
                valute.value / valute.nominal
            )

            et.indent(elem)
            xml_str = et.tostring(elem, encoding="unicode")

        return xml_str

    # Форма ошибки XML
    @staticmethod
    async def get_error_xml() -> str:
        elem = et.Element("ValCurs")
        elem.text = " Error in parameters "
        et.indent(elem)
        xml_str = et.tostring(elem, encoding="unicode")
        return xml_str

    @staticmethod
    async def load_data() -> list[ValuteRange]:
        with open("data.json", "r", encoding="utf-8") as f:
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
