import json

d1 = {
    'pessoa1': {
        'nome': 'claudio',
        'idade': 25
    },
    'pessoa2': {
        'nome': 'natalia',
        'idade': 24
    }
}

# convertendo o dicionario para json
d1_json = json.dumps(d1, indent=True)

with open('abc3.json', 'w+') as file:
    file.write(d1_json)