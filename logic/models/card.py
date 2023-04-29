import logic.validators.card as validator
from jsonschema import validate
from database.schemas.card import card as collection

from errors.database import NoOperationsError

from typing import Union

def saved_list(params: dict) -> list:
    validate(params, validator.saved_list) # if no exception validation passed
    result = collection.find_one({"userNo":params["userNo"]})

    if result is None:
        raise NoOperationsError("No users found!")
    else:
        return result["allCards"]

def save_card(params: dict) -> bool:
    validate(params, validator.save_card) # if no exception validation passed

    result = collection.update_one({"userNo":params["userNo"]}, 
                                   {"$push":{"allCards":params["cardNumber"]}})

    if result.modified_count == 0:
        raise NoOperationsError("No users found!")

    return True

def saved_payment(params: dict) -> Union[int, float]:
    validate(params, validator.saved_payment) # if no exception validation passed

    user = collection.find_one({"userNo":params["userNo"]})
    if user is None:
        raise NoOperationsError("No users found!")
    if user["balance"] < params["payment"]:
        raise NoOperationsError("Not enough money!")
    
    result = collection.update_one({"userNo":params["userNo"]}, { "$inc": { "balance": -params["payment"] } })
    if result.modified_count == 0:
        raise NoOperationsError("Payment failed!")

    return user["balance"] - params["payment"]


def cancel_payment(params: dict) -> Union[int, float]:
    validate(params, validator.cancel_payment) # if no exception validation passed

    user = collection.find_one({"userNo":params["userNo"]})
    if user is None:
        raise NoOperationsError("No users found!")
    
    result = collection.update_one({"userNo":params["userNo"]}, { "$inc": { "balance": params["payment"] } })
    if result.modified_count == 0:
        raise NoOperationsError("Cancel failed!")

    # TODO add payment history for per card
