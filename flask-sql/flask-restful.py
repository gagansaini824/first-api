from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'


jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {'item':item}, 200 if item else 404
    
    def post(self, name):
        
        if next(filter(lambda x: x['name']==name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}
        
        data =  request.get_json()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201
    
    
class ItemList(Resource):
    def get(self):
        return {'items':items}
    
    


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)