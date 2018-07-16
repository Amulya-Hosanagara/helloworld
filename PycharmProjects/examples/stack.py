from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self, item):
        return self.item.pop()
    def size(self):
        return len(self.items)

s = Stack()
s.push(7)
s.push(8)
print(s.size())

#api.add_resource(Stack, '/')

#if __name__ == "__main__":
#    app.run(debug=True)

