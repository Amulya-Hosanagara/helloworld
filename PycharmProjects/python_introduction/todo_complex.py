from flask import Flask
from flask_restful import Resource, Api, request, reqparse

app = Flask(__name__)
api = Api(app)

todos = {
    'todo1': {'hai'},
    'todo2': {'?????'},
    'todo3': {'Good morning!'}
}

parser = reqparse.RequestParser()
parser.add_argument('task')

class ToDoTask(Resource):
    def get(self, todo_id):
        return todos[todo_id]
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        return task, 201
    def delete(self, todo_id):
        del todos[todo_id]
        return '', 201

class ToDoList(Resource):
    def get(self):
        return todos
    def post(self, todo_id):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = {'task': args['task']}
        return todos[todo_id], 201

api.add_resource(ToDoList, '/todos')
api.add_resource(ToDoTask, '/todos/<todo_id>')

if __name__=="__main__":
    app.run(debug=True)