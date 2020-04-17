
from flask_restful import Resource
from models import Users
from settings import db
from models import serialize_multiple


class AllUsers(Resource):

    @staticmethod
    def get():
        return serialize_multiple(Users.query.all())


class SingleUser(Resource):
    @staticmethod
    def get(user_id):
        return Users.query.get(user_id).serialize()

    @staticmethod
    def delete(user_id):
        db.session.query(Users).filter_by(id=user_id).delete()
        db.session.commit()
        return {}, 200
