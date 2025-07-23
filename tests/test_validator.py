import pytest


@pytest.mark.asyncio
async def test_validate_date_correct_formats(validator):
    valid_dates = ["01/01/2023", "31.12.2023", "15/06/2024", "01.01.1970"]

    for date in valid_dates:
        assert await validator.validate_date(date) is True


@pytest.mark.asyncio
async def test_validate_date_incorrect_formats(validator):
    invalid_dates = [
        "2023-01-01",
        "01-01-2023",
        "32.01.2023",
        "01/13/2023",
        "asdfg",
        "12345678",
    ]

    for date in invalid_dates:
        assert await validator.validate_date(date) is False
