


class ProductInMemoryDb:
    product_list=[]
    def add(self,dict:dict):
        ProductInMemoryDb.product_list.append(dict)
    def update(self,id:int,dict:dict):
        for item in ProductInMemoryDb.product_list:
            if item['id']==id:
                item.insert(dict)
    