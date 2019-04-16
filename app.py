from flask import Flask,jsonify, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## returns either work, or rip
class key_value(Resource):

	def get(self, key):
		thisdict = {'test': 'tester'}
		if key in thisdict:
			return make_response(jsonify(doesExist=True, message="Retrieved successfully", value="Data Structures"), 200)
		else:
			return make_response(jsonify(doesExist=False, error="Key does not exist", message="Error in GET"), 404)

	def put(self, key):
		thisdict = {'test': 'tester'}
		if len(key) < 50:
			message = request.get_json()
			if key in thisdict: ## edit the message
				if message.get('value'):## data exists
					thisdict[key] = message.get('value')
					return make_response(jsonify(message="Updated successfully",replaced=True), 200)
				else: ## data nonexistent
					return make_response(jsonify(error="Value is missing",message="Error in PUT"), 400)
			else: ##add a new message at key
				if message.get('value'): ##data exists
					##change message of 'key'
					thisdict[key] = message.get('value')
					return make_response(jsonify(message="Added successfully",replaced=False), 201)
				else: ##data nonexistent
					return make_response(jsonify(error="Value is missing",message="Error in PUT"), 400)
		else:
			return make_response(jsonify(error="Key is too long", message="Error in PUT"), 400)

api.add_resource(key_value, '/key-value-store/<key>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
