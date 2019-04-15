from flask import Flask,jsonify, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class key_value(Resource):

	def get(self, key):
		thisdict = {'test': 'tester'}
		if key in thisdict:
			return make_response('work', 200)
		else:
			return make_response('rip',200)

api.add_resource(key_value, '/key-value-store/<key>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)