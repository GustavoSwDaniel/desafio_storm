from typing import Any, Dict, List, Tuple

facts = [
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]

schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]

def get_data_by_cardinality(
    data_list: List[Dict[str, Any]], 
    name: str, 
    data_type: str, 
    cardinality: str
) -> Any:
    """
    Obtém dados com base na cardinalidade especificada.

    Args:
        data_list (List[Dict[str, Any]]): Lista de dados a serem filtrados.
        name (str): Nome para filtrar os dados.
        data_type (str): Tipo de dado a ser filtrado.
        cardinality (str): Cardinalidade ('one' ou 'many').

    Returns:
        Any: O último item ativo se a cardinalidade for 'one';
             caso contrário, retorna uma lista de itens ativos.
    """
    filtered_data = [item for item in data_list if item['name'] == name and item['type'] == data_type and item['active']]
    if cardinality == 'ONE':
        return filtered_data[-1] if filtered_data else None
    return filtered_data

def data_process(schema: List[Tuple[str, str, str]], data_list: List[Tuple[str, str, str, bool]]) -> None:
    """
    Processa os dados de entrada com base no esquema e imprime os resultados.

    Args:
        schema (List[Tuple[str, str, str]]): Esquema de cardinalidade a ser aplicado.
        data_list (List[Tuple[str, str, str, bool]]): Lista de dados a serem processados.

    Returns:
        None: Esta função imprime os resultados processados.
    """
    # Formata os dados de entrada
    data_formatted = [{'name': data[0], 'type': data[1], 'address': data[2], 'active': data[3]} for data in data_list]
    schema_formatted = [{'type': data[0], 'cardinality': data[2]} for data in schema]

    response = []
    for data in data_formatted:
        for rule in schema_formatted:
            if rule['type'].upper() == data['type'].upper():
                processed_data = get_data_by_cardinality(data_formatted, data['name'], data_type=data['type'], cardinality=rule['cardinality'].upper())
                
                if isinstance(processed_data, dict):
                    data_reconverted = (processed_data['name'], processed_data['type'], processed_data['address'], processed_data['active'])
                    if data_reconverted not in response:
                        response.append(data_reconverted)

                elif isinstance(processed_data, list):
                    for info in processed_data:
                        data_reconverted = (info['name'], info['type'], info['address'], info['active'])
                        if data_reconverted not in response:
                            response.append(data_reconverted)

    return response

response = data_process(schema=schema, data_list=facts)

for resp in response:
    print(resp)