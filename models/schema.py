allCardsSchema = {
    'type': 'array',
    'minItems': 0,
}

baseSchema = {
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
    "additionalProperties": False,
    "required": []
}