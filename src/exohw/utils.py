import json

def load_json_file(filepath: str) -> dict:
    """Load and return data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)