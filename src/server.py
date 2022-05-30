import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ast
from HealthyFoodController import healthyfood_bp
from HealthyUserController import healthyuser_bp


app = Flask(__name__)

app.register_blueprint(healthyfood_bp, url_prefix='/healthy-food')
app.register_blueprint(healthyuser_bp, url_prefix='/healthy-user')

port = int(os.environ.get('PORT', 3000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

