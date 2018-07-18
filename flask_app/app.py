from flask import request
from flask_restful import reqparse, Resource

from config.app import api, db, app
from config.models import User
# from scripts.manage import Manager, manager

class UserResource(Resource):
    def get(self, user_id):
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            return {'message': 'Not found'}, 404
        return {user_id: user}

    def put(self, user_id):
        user = db.query(User).filter_by(id=user_id)
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        return {user_id: user}


class UserList(Resource):

    def get(self):
        return [{user.id: {'name': user.name, 'email': user.email}} for user in db.session.query(User).all()]

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id')

        parser.add_argument('name')
        parser.add_argument('email')
        args = parser.parse_args()

        if not 'name' in args or not 'email' in args:
            # we return bad request since we require name and color
            return {'message': 'Missing required parameters.'}, 400

        new_user = User(id= args['id'], name=args['name'], email=args['email'])
        db.session.add(new_user)
        db.session.commit()

        return {new_user.id: {'id': new_user.id, 'name': new_user.name, 'email': new_user.email}}, 201


api.add_resource(UserResource, '/user/<user_id>')
api.add_resource(UserList, '/user')

if __name__=="__main__":
    app.run()
