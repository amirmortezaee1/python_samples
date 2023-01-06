class ProductInMemoryDb:
    __product_list = []
    
    
    def __init__(self):
        pass
    
    def insert(self, product):
        self.__product_list.append(product)
        return product
    
    def read(self, id:int):
        for product in self.__product_list:
            if product['id'] == id:
                return product
        return f"This id '{id}' does not exist"
    
    def update(self, id, new_attr):
        for product in self.__product_list:
            if product['id'] == id:
                for key, value in new_attr.items():
                    if key in product:
                        product[key] = value
                return 'Done'
        return 'This obj does not  exist'
    
    def delete(self, id):
        for product in self.__product_list:
            if product['id'] == id:
                self.__product_list.remove(product)
                return 'Done'
        return f"this is '{id}' does not exist"
    
    
    def list_all(self):
        return self.__product_list