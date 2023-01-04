


class ProductInMemoryDb:
    product_list=[]
    def insert(self,dict:dict):
        ProductInMemoryDb.product_list.append(dict)
