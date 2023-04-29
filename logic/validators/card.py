from helpers.required import required
from database.schemas.card import schema

save_card = required(
    schema,
    {
        'userNo': {'type': 'number'}, 
        'cardNumber': {'type': 'number'}
    }
)

saved_payment = required(
    schema,
    {
        'userNo': {'type': 'number'}, 
        'payment': {'type': 'number'}
    }
)

cancel_payment = required(
    schema,
    {'userNo': {'type': 'number'}, 'payment': {'type': 'number'}}
)

saved_list = required(
    schema,
    {'userNo': {'type': 'number'}}
)