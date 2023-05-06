import pytest
import datetime as dt


from src.utils import (
    get_datetime,
    get_date
)


def test_get_datetime():
    assert isinstance(get_datetime(), dt.datetime)


def test_get_date(mocker):
    assert isinstance(get_date(), dt.date)
    with mocker.patch("src.utils.get_datetime", return_value=dt.datetime(11, 11, 11)):
        assert get_date() == dt.datetime(11, 11, 11).date()
