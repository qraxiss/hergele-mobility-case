from database.schemas.schema import Schema
allCardsSchema = {
    'type': 'array',
    'minItems': 0,
}

schema = {
    "type": "object",
    "properties": {
        "userNo": {'type': 'number'},
        "authCode": {'type': 'string'},
        "name": {'type': 'string'},
        "surname": {'type': 'string'},
        "birthDate": {'type': 'string'},
        "phoneNumber": {'type': 'number'},
        "email": {'type': 'string'},
        "selectedCard": {'type': 'string'},
        "allCards": allCardsSchema,
        "balance": {'type': 'number'},
    },
    "required": ["userNo"]
}

card = Schema('card', schema)