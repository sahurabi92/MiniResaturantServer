from flask_mongoengine import MongoEngine
from mongoengine import *
from flask_restplus import Api

api = Api(title='Restaurant server',
          version='1.0',
          description='Restaurant server')
mongodb = MongoEngine()



class Table(mongodb.Document):

    number = IntField(required=True, unique=True)
    status = IntField(required=True)



    def to_json(self):
        return {"number": self.number,
                "status": self.status}


class Menu(mongodb.Document):

    item_name = StringField(max_length=20, required=True)
    category = StringField(max_length=20, required=True, choices=('veg', 'non-veg'))
    price = IntField(required=True)


    def to_json(self):
        return {"item_name": self.item_name,
                "category": self.category, 'price':self.price}


class Orders(mongodb.Document):
    customer_name = StringField(max_length=50, required=True)
    phone_number = IntField(required=True)
    items = ListField(StringField( max_length=120), required=True)
    table_number = IntField(required=True)
    order_status = IntField(required=True, choices=(1,2,3,4))

    def to_json(self):
        return {"customer_name": self.customer_name,
                "phone_number": self.phone_number, 'items':self.items, 'table_number':self.table_number}
