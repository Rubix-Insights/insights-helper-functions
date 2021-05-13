import pytest
import datetime
from rubixinsights.helper import extract_components_from_execution_date

def test_extract_components_from_execution_date():
    execution_date = datetime.date.fromisoformat('2021-01-01')
    year, month, day = extract_components_from_execution_date(execution_date)
    assert year == '2021'
    assert month == '01'
    assert day == '01'
