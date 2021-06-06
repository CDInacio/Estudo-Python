import json

with open('abc3.json', 'r') as file:
    d1_json = file.read()
    # convertendo o json de volta para dicionario
    d1_json = json.loads(d1_json)


for key, value in d1_json.items():
    print(key)
    for key1, value1 in value.items():
        print(f'{key1}: {value1}')
