from flask_restful import Resource, request
import logic.models.card as card

from errors.handler import handler

class SavedList(Resource):
    @handler
    def get(self):
        return card.saved_list(request.json)

class SaveCard(Resource):
    @handler
    def post(self):
        return card.save_card(request.json)

class SavedPayment(Resource):
    @handler
    def post(self):
        return card.saved_payment(request.json)

class CancelPayment(Resource):
    @handler
    def post(self):
        return card.cancel_payment(request.json)