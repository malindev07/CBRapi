import pytest
from xml.etree import ElementTree as et


@pytest.mark.asyncio
async def test_get_successful_xml(service, valutes_config):
    date_req = "01/01/2023"
    xml_content = await service.get_successful_xml(date_req, valutes_config.valutes)

    assert isinstance(xml_content, str)

    root = et.fromstring(xml_content)
    assert root.tag == "ValCurs"
    assert root.attrib["Date"] == date_req
    assert root.attrib["name"] == "Foreign Currency Market"

    assert len(root.findall("Valute")) > 0


@pytest.mark.asyncio
async def test_get_error_xml(service):
    xml_content = await service.get_error_xml()

    assert isinstance(xml_content, str)

    root = et.fromstring(xml_content)
    assert root.tag == "ValCurs"
    assert "Error in parameters" in root.text
