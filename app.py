from flask import Flask,jsonify, request, make_response, g
from flask_restful import Api, Resource
import sqlite3
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASE = os.path.join(PROJECT_ROOT, 'sql', 'dict.db')

app = Flask(__name__)
api = Api(app)

#initialize db
def get_db():
    db = sqlite3.connect(DATABASE)
    return db

#closes db after a get/post/etc request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_dict', None)
    if db is not None:
        db.close()

## returns either work, or rip
class key_value(Resource):
	def get(self, key):
		conn = get_db()
		cur = conn.cursor()
		value = query_db('select value from dict where key = ?', (key,))
		db_key = query_db('select key from dict where key = ?', (key,))
		if db_key is None:
			return make_response(jsonify(doesExist=False, error="Key does not exist", message="Error in GET"), 404)
		else:
			return make_response(jsonify(doesExist=True, message="Retrieved successfully", value=value), 200)
		# if key in thisdict:
		# 	return make_response(jsonify(doesExist=True, message="Retrieved successfully", value="Data Structures"), 200)
		# else:
		# 	return make_response(jsonify(doesExist=False, error="Key does not exist", message="Error in GET"), 404)

	def put(self, key):
		conn = get_db()
		cur = conn.cursor()
		test = (key,)
		db_key = query_db('select key from dict where key = ?', test)
		value = request.args.get('value')
		if db_key is None:
			cur.execute("INSERT INTO dict VALUES('tea', 'apple')")
			conn.commit()
			return make_response("get in here", 200)
		else:
			return make_response("not in here",200)

		# if key in thisdict:
		# 	thisdict.update(key = request.args.get('value'))
		# 	return make_response(jsonify(message="Updated successfully",replaced=True), 200)
		# else:
		# 	thisdict.update(key = request.args.get('value'))
		# return make_response(jsonify(message="Added successfully",replaced=False), 201)

# Query Function
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


#initialize db schemea
# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()





api.add_resource(key_value, '/key-value-store/<key>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
