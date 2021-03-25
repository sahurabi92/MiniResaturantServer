def init_api(api):
    from .view import TableManagement, MenuManagement, OrderManagement, OrderStatus
    api.add_resource(TableManagement,
                     '/api/v1/table/', methods =['GET', 'POST', 'DELETE']
                     )
    api.add_resource(MenuManagement,
                     '/api/v1/menu/',methods=['GET', 'POST']
                     )
    api.add_resource(MenuManagement,
                     '/api/v1/menu/<menu_id>', methods=['PUT', 'DELETE']
                     )
    api.add_resource(OrderManagement,
                     '/api/v1/order', methods=['POST', 'GET']
                     )
    api.add_resource(OrderManagement,
                     '/api/v1/order/<bookid>', methods=['DELETE', 'PATCH']
                     )
    api.add_resource(OrderStatus,
                     '/api/v1/order/<status>', methods=['GET']
                     )
