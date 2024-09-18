import json
import os

DATA_FILE = 'words.json'

# Function to load words from the JSON file
def load_words():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save words to the JSON file
def save_words(words):
    with open(DATA_FILE, 'w') as file:
        json.dump(words, file, indent=4)
