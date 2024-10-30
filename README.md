# Desafio Backend Python - STORM

Este repositório contém a implementação do desafio para a posição de desenvolvedor Backend na STORM.

## Descrição do Desafio

O desafio consiste em desenvolver uma função que processe uma lista de registros, ou "fatos", e um esquema de cardinalidade dos atributos das entidades. Cada registro representa um fato sobre uma entidade, e o objetivo é retornar os fatos vigentes, ou seja, as informações atuais sobre cada entidade.

### Exemplo de Fatos e Esquema

A lista `facts` contém registros no formato `(entidade, atributo, valor, ativo)`, onde `ativo` indica se o valor está atualmente associado ao atributo ou se foi removido. Exemplo:

```python
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
```

O esquema schema define a cardinalidade dos atributos:

```python
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]
```

### Resultado esperado é 

```python
[
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]
```

### Estrutura do projeto

```bash
.
├── desafio.py               # Script principal do projeto
├── __pycache__              # Cache de arquivos compilados
├── README.md                # Documentação do projeto
├── requirements.txt         # Dependências do projeto
└── tests                    # Testes unitários
    ├── data_test.py         # Dados de teste
    └── test_desafio.py  
```

### Instruções de intação

1 - Clone o repositório:

```bash
    git clone https://github.com/GustavoSwDaniel/desafio_storm.git
```

2 - Navegue até o diretório do projeto:

```bash
    cd desafio_storm
```

3 - Crie um ambiente virtual:
```bash
    python3 -m venv venv
```

4 - Ative o ambiente virtual:
* Linux/MacOS
    ```bash
        source venv/bin/activate
    ```
* Windows
    ```bash 
        venv\Scripts\activate
    ```
5 - Instale as dependências:
```bash
    pip install -r requirements.txt
```

### Como executar 
```bash
    python desafio.py
```

### Testes
Foi criando um arquivo chamando data_test.py onde contem os casos de teste utilizando no teste unistario

```bash
    pytest tests/
```

ou apenas
```bash
    pytest
```

## Considerações finais 

Esse projeto foi desenvolvido com foco em boas práticas de código, organização e modularização para garantir legibilidade e fácil manutenção.