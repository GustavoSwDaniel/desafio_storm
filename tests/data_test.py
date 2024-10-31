data = [
    {
        "data" : [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
        ],
        "schema": [
            ('endereço', 'cardinality', 'one'),
            ('telefone', 'cardinality', 'many')
            ],
        "expected":[
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ],
    },
    {
        "data" : [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '56789-1018', True),
            ('gabriel', 'telefone', '56789-1013', True),
            ('gabriel', 'telefone', '56789-1012', True),
        ],
        "schema": [
            ('endereço', 'cardinality', 'one'),
            ('telefone', 'cardinality', 'many')
            ],
        "expected":[
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '56789-1018', True),
            ('gabriel', 'telefone', '56789-1013', True),
            ('gabriel', 'telefone', '56789-1012', True),
            ],
    },
    {
        "data" : [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'endereço', 'rua dos alfeneiros, 4', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '56789-1018', True),
            ('gabriel', 'telefone', '56789-1013', True),
            ('gabriel', 'telefone', '56789-1012', True),
        ],
        "schema": [
            ('endereço', 'cardinality', 'many'),
            ('telefone', 'cardinality', 'many')
            ],
        "expected":[
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'endereço', 'rua dos alfeneiros, 4', True),
            ('joão', 'telefone', '91234-5555', True),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '56789-1018', True),
            ('gabriel', 'telefone', '56789-1013', True),
            ('gabriel', 'telefone', '56789-1012', True),
        ],
    },
    {
        "data" : [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True),
            ('gabriel', 'telefone', '56789-1018', True),
            ('gabriel', 'telefone', '56789-1011', True),
            ('gabriel', 'telefone', '56789-1012', True),
        ],
        "schema": [
            ('endereço', 'cardinality', 'one'),
            ('telefone', 'cardinality', 'one')
            ],
        "expected":[
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '91234-5555', True),
            ('gabriel', 'telefone', '56789-1012', True),
        ],
    }

]