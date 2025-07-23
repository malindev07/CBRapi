import json
import random
from dataclasses import dataclass
from xml.etree import ElementTree as et

from config.config_model import ValuteRange
from valute_model import Valute


@dataclass
class Service:

    # Рандомные валюты
    @staticmethod
    async def get_random_valutes_count(valutes: list[ValuteRange]) -> list[Valute]:
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
    async def get_successful_xml(
        self, date_req: str, valutes: list[ValuteRange]
    ) -> str:
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
