import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='price cannot be converted'
                        )



    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name '{}' has existed".format(name)}, 400

        data = Item.parser.parse_args()
        new_item = ItemModel(name=name, price=data['price'])
        new_item.save_to_db()
        return new_item.json(), 201


    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # Find the item with the given name
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']   
        else:
            item = ItemModel(name=name, price=data['price'])
        item.save_to_db()
        
        return item.json(), 200

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            print(type(item))
            item.delete_from_db()
            return {'message': 'Item is deleted'}
        return {'message': 'Item not found'}


class ItemList(Resource):
    def get(self):
        items = ItemModel.query.all()

        if items:
            return {'item': [item.json() for item in items]}, 200
        return {"message": "Items not found"}, 404
