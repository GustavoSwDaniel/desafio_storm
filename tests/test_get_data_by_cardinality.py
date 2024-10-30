from main import get_data_by_cardinality

def test_get_data_by_cardinality_one():
    data_list = [
        {'name': 'joao', 'type': 'telefone', 'value': '1234-5678', 'active': True},
        {'name': 'joao', 'type': 'telefone', 'value': '2345-6789', 'active': True},
        {'name': 'joao', 'type': 'telefone', 'value': '3456-7890', 'active': False},
    ]
    
    result = get_data_by_cardinality(data_list, 'joao', 'telefone', 'ONE')
    assert result == {'name': 'joao', 'type': 'telefone', 'value': '2345-6789', 'active': True}


def test_get_data_by_cardinality_many():
    data_list = [
        {'name': 'joao', 'type': 'telefone', 'value': '1234-5678', 'active': True},
        {'name': 'joao', 'type': 'telefone', 'value': '2345-6789', 'active': True},
        {'name': 'joao', 'type': 'telefone', 'value': '3456-7890', 'active': False},
    ]
    
    result = get_data_by_cardinality(data_list, 'joao', 'telefone', 'MANY')
    assert result == [
        {'name': 'joao', 'type': 'telefone', 'value': '1234-5678', 'active': True},
        {'name': 'joao', 'type': 'telefone', 'value': '2345-6789', 'active': True}
    ]


def test_get_data_by_cardinality_no_active_items():
    data_list = [
        {'name': 'joao', 'type': 'telefone', 'value': '1234-5678', 'active': False},
        {'name': 'joao', 'type': 'telefone', 'value': '2345-6789', 'active': False},
    ]
    
    result_one = get_data_by_cardinality(data_list, 'joao', 'telefone', 'ONE')
    result_many = get_data_by_cardinality(data_list, 'joao', 'telefone', 'MANY')
    
    assert result_one is None
    assert result_many == []
