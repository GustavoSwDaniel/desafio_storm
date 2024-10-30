
import pytest
from main import data_process
from tests import data_test

test_data = []
for i in data_test.data:
    test_data.append((i['data'], i['schema'], i['expected']))

@pytest.mark.parametrize("data, schema, expected", test_data)
def test_data_process(data, schema, expected):
    response = data_process(schema=schema, data_list=data)
    assert response == expected