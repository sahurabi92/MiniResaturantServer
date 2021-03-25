import json

from flask import request, jsonify, make_response
from .models import Table, Menu, Orders
from flask_restplus import Resource, fields
from . import  api

"""Handling all the Operation in this file"""

delete_table = api.model('delete table', {
    'id': fields.String})
add_table = api.model('add table', {
    'table_number': fields.Integer, 'status': fields.Integer})


class TableManagement(Resource):

    @api.expect(add_table)
    def post(self):
        """ Post Method to add the table"""
        try:
            records = json.loads(request.data)
            data = Table(number=records['table_number'],
                         status=records['status'])
            data.save()
            return jsonify(data.to_json())
        except Exception:
            return make_response({"msg": "Bad Request"}, 400)

    def get(self):
        """Get Method to view all the table"""
        data = Table.objects.all()
        return jsonify(data)

    @api.expect(delete_table)
    def delete(self):
        """Delete Method to delete the added table"""
        try:
            records = json.loads(request.data)
            data = Table.objects.get_or_404(id=records['id'])
            Table.delete(data)
            return "Delete Done", 201
        except Exception as e:
            print(e)
            return f"Error Occurred: {e}"


add_menu = api.model('Add Menu', {
    'item_name': fields.String, 'category': fields.String, 'price': fields.Integer})
update_menu = api.model('Add Menu', {
    'item_name': fields.String, 'category': fields.String, 'price': fields.Integer}, required=False)


class MenuManagement(Resource):
    """This Class is for Menu management"""

    @api.expect(add_menu)
    def post(self):
        """ Post Method to add the Menu"""
        try:
            records = json.loads(request.data)
            data = Menu(item_name=records['item_name'],
                        category=records['category'],
                        price=records['price']
                        )
            data.save()
            return jsonify(data.to_json())
        except Exception as e:
            return make_response({"msg": f"Bad Request {e}"}, 400)

    def get(self):
        """Get Method to view all the Menus"""
        data = Menu.objects.all()
        return jsonify(data)

    @api.expect(update_menu)
    def put(self, menu_id):
        """ Put method to update the menu using id"""
        try:
            payload = request.get_json()
            obj = Menu.objects.get_or_404(id=menu_id)
            obj.update(**payload)
            return f"Updated data {jsonify(payload)}", 200
        except Exception as e:
            return {"msg": f"Bad Request: {e}"}, 400

    @api.doc(params={"menu_id": "ID of Menu"})
    def delete(self, menu_id):
        """Delete Method to delete the Menus"""
        try:
            data = Menu.objects.get_or_404(id=menu_id)
            Table.delete(data)
            return "Delete Done", 201
        except Exception as e:

            return f"Error Occurred: {e}", 401


updateOrder_status = api.model('Update order status', {
    'status': fields.Integer}, required=True)

add_order = api.model('Add Order', {
    'customer_name': fields.String, 'phone_number': fields.Integer,
    'items': fields.List(fields.String), 'table_number': fields.Integer})
change_order = api.model('change order status Order', {
    'status': fields.Integer})


class OrderManagement(Resource):
    """This Class is for Order management"""

    @api.expect(add_order)
    def post(self):
        """ Post Method to add the order"""
        try:
            records = json.loads(request.data)
            data = Orders(customer_name=records['customer_name'],
                          phone_number=records['phone_number'],
                          items=records['items'],
                          table_number=records['table_number'],
                          order_status=1
                          )
            data.save()
            return jsonify(data.to_json())
        except Exception as e:
            return make_response({"msg": f"Bad Request {e}"}, 400)

    @api.doc({"msg":"To get all the data"})
    def get(self):
        """Get Method to view all the Menus"""
        data = Orders.objects.all()
        return jsonify(data)

    @api.doc(params={"ID": "Order ID"})
    @api.expect(change_order)
    def patch(self, bookid):
        """ Put method to update the menu using order id"""
        try:
            payload = request.json['status']
            obj = Orders.objects.get_or_404(id=bookid)
            print(payload)
            obj.update(order_status=payload)
            return f"Order status is updated", 200
        except Exception as e:
            return {"msg": f"Bad Request: {e}"}, 400

    @api.doc(params={"ID": "Order ID"})
    def delete(self, bookid):
        """Delete Method to delete the Order"""
        try:
            data = Orders.objects.get_or_404(id=bookid)
            Table.delete(data)
            return "Delete Done", 201
        except Exception as e:
            return f"Error Occurred: {e}", 401


status_details = {
    "placed": 1,
    "going": 2,
    "completed": 3,
    "canceled": 4,
}


class OrderStatus(Resource):
    @api.doc(params={"status":"(placed, going, completed, canceled)"})
    def get(self, status):
        """Get the Order status by selecting the status type (placed, going, completed, canceled)"""
        try:
            val = status_details[status]
            data = Orders.objects(order_status=val)
            return jsonify(data)
        except KeyError:
            return "Invalid status details given"
        except Exception as e:
            print(e)
            return "Bad Request", 400
