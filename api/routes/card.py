import api.controllers.card as controller
from flask import current_app as app
from flask_restful import Api

api = Api(app)

api.add_resource(controller.SavedList, '/saved-list')
api.add_resource(controller.SaveCard, '/save-card')
api.add_resource(controller.SavedPayment, '/saved-payment')
api.add_resource(controller.CancelPayment, '/cancel-payment')
