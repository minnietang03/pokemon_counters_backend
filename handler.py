import json
from pokemon_backend_data import read_pokemon_dict


def lambda_handler(event, context):
    pokemon_dict = read_pokemon_dict()
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
            "Access-Control-Allow-Headers": "Content-Type",  # Allow Content-Type header
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS"  # Allow GET, POST, and OPTIONS methods
        },
        "body": json.dumps(pokemon_dict)
        # "body": "this is a test change."
    }


