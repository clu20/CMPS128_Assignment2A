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

	def post(self, key):
		thisdict = {'test': 'tester'}
		if key in thisdict:
			return make_response(jsonify(message="Added successfully",replaced=false), 201)
		else:
			return make_response(jsonify(message="Updated successfully",replaced=true), 200)


api.add_resource(key_value, '/key-value-store/<key>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
