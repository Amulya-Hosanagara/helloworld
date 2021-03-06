from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

todos = {}

class ToDoSimple(Resource):
    def get(self, todo_id):
        return todos
    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(ToDoSimple, '/<string:todo_id>')

if __name__=="__main__":
    app.run(debug=True)