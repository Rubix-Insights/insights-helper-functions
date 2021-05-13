import pytest
from collections import namedtuple
from rubixinsights.metadata import Metadata

@pytest.fixture
def business_key():
    BusinessKey = namedtuple('BusinessKey', ['account', 'report_name', 'attribution_model', 'execution_date'])
    bk = BusinessKey(account='test', report_name='test', attribution_model = '1d_view', execution_date = '2021-03-24')
    return bk

@pytest.fixture
def metadata():
    metadata = Metadata(
            host = "localhost",
            port = "5432",
            username = "postgres",
            password = "postgres",
            database = "postgres",
            data_source = 'facebook'
    )
    return metadata



# metadata.update_as_succeeded("test", "test", "2021-01-01")

def test_validate_if_need_the_load(metadata, business_key):
    metadata.validate_if_need_the_load(business_key)
    # assert 0==1

def test_update_as_succeeded(metadata, business_key):
    metadata.update_as_succeeded(business_key)
    # assert 0==1