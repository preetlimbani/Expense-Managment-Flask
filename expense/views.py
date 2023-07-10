from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource
from bson.objectid import ObjectId
from expense import mongo
from expense.models import Expense, User
from .schema import ExpenseSchema


class RegisterView(Resource):
    def post(self):
        data = request.get_json()
        if 'username' not in data or 'password' not in data:
            return {'error': 'Missing username or password'}, 400
        existing_user = User.find_by_username(data['username'])
        if existing_user:
            return {'error': 'Username already exists'}, 409
        user = User(data['username'], data['password'])
        user.save()
        return {'message': 'User registered successfully'}, 201


class LoginView(Resource):
    def post(self):
        data = request.get_json()
        if 'username' not in data or 'password' not in data:
            return {'error': 'Missing username or password'}, 400
        user = User.find_by_username(data['username'])
        if not user or not User.verify_password(user['password'], data['password']):
            return {'error': 'Invalid username or password'}, 401
        access_token = create_access_token(identity=str(user['_id']))
        return {'access_token': access_token}, 200


class ExpenseListCreateView(Resource):
    decorators = [jwt_required()]

    def get(self):
        user_id = get_jwt_identity()
        expenses = mongo.db.expenses.find({'user_id': user_id})
        serialized_data = ExpenseSchema().dump(expenses, many=True)
        return {'expenses': serialized_data}, 200

    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        expense = Expense(user_id, data['amount'], data['title'])
        expense.save()
        return {'message': 'Expense created successfully'}, 201


class ExpenseView(Resource):
    decorators = [jwt_required()]

    def get(self, id):
        user_id = get_jwt_identity()
        expense = mongo.db.expenses.find_one({'user_id': user_id, '_id': ObjectId(id)}, {'_id': 0})
        if not expense:
            return {'error': 'Expense not found'}, 404
        serialized_data = ExpenseSchema().dump(expense)
        return {'expense': serialized_data}, 200

    def put(self, id):
        user_id = get_jwt_identity()
        data = request.get_json()
        updated = mongo.db.expenses.update_one(
            {'user_id': user_id, '_id': ObjectId(id)},
            {'$set': {'amount': data['amount'], 'description': data['title']}}
        )
        if not updated:
            return {'error': 'Expense not found'}, 404
        return {'message': 'Expense updated successfully'}, 200

    def delete(self, id):
        user_id = get_jwt_identity()
        deleted = mongo.db.expenses.delete_one({'user_id': user_id, '_id': ObjectId(id)})
        if not deleted.deleted_count:
            return {'error': 'Expense not found'}, 404
        return {'message': 'Expense deleted successfully'}, 200
