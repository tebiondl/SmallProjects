import json

def load_data(id):
    try:
        with open(f'data{id}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(id, data):
    with open(f'data{id}.json', 'w') as file:
        json.dump(data, file)
        
def remove_data(id):
    open(f'data{id}.json', 'w').close()