from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name_Delete(Resource):
	def delete(self, employee_id):
		conn = db_connect.connect()
		query = conn.execute("delete from employees where EmployeeId = %d" %int(employee_id))

class Employees_Title_Update(Resource):
	def post(self, employee_id):
		conn = db_connect.connect()
		newTitle = request.data
		sql = "update employees set title=? where EmployeeId=?"
		conn.execute(sql,(newTitle,employee_id))
		
	

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(Employees_Name_Delete,'/employees_delete/<employee_id>') #teste com remocao
api.add_resource(Employees_Title_Update,'/employees_update/<employee_id>') #atualiza titulo


if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5002')
