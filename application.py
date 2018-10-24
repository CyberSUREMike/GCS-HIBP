<<<<<<< HEAD
#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource, reqparse
from hibp import *

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, email):
        data = getAllBreachesForAccount(email)
        return data, 200

class Breach(Resource):

    def get(self, name):
        data = getBreachData(name)
        return data, 200

api.add_resource(User, "/user/<string:email>")
api.add_resource(Breach, "/breach/<string:name>")

app.run(debug=True)
=======
#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource, reqparse
from hibp import *

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, email):
        data = getAllBreachesForAccount(email)
        return data, 200

class Breach(Resource):

    def get(self, name):
        data = getBreachData(name)
        return data, 200

api.add_resource(User, "/user/<string:email>")
api.add_resource(Breach, "/breach/<string:name>")

app.run(debug=True)
>>>>>>> 3ea0d4bb6491210789cbe40ff787881803a3df65
