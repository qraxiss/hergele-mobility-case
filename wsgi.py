from flask import Flask, request
from api.middlewares.auth import UserAuthMiddleware as middleware

app = Flask(__name__)
app.wsgi_app = middleware(app.wsgi_app)

with app.app_context():
    import api.routes.card

if __name__ == "__main__":
    app.run(port=8000, debug=True)