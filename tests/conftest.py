import json
from pathlib import Path

import pytest
from httpx import AsyncClient

from main import app
from service import Service
from api.validator import Validator
from config.config_model import ValutesConfig, ValuteRange


@pytest.fixture
def service():
    return Service()


@pytest.fixture
def validator():
    return Validator()


@pytest.fixture
def test_data_path():
    return Path(__file__).parent / "test_data.json"


@pytest.fixture
def valutes_config(test_data_path):
    with open(test_data_path, "r", encoding="utf-8") as f:
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

        return ValutesConfig(valutes=data)
