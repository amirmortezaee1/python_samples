class ProductInMemoryDb:
    _product_list = []


    def __init__(self):
        pass

    def insert(self, product_dict: dict):
        self._product_list.append(product_dict)

    def read(self, id:int):
        for product_dict in self._product_list:
            if product_dict["id"] == id:
                return product_dict
        return "input id doesn't exist"

    def update(self, id, new_attr):                                     
        for product_dict in self._product_list:
            if product_dict["id"] == id:
                for key, value in new_attr.items():
                    if key in product_dict:
                        product_dict[key] = value
                return "updated"
        return "object does not exist"
    
    def delete(self, id):
        for product_dict in self._product_list:
            if product_dict["id"] == id:
                self._product_list.remove(product_dict)
                return "deleted"
        return "falied to delete it"

    def show_all(self):
        return self._product_list