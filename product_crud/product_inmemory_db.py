
class ProductInMemoryDb:
    product_list=[]

    def __init__(self):
        pass
    @classmethod
    def add(cls,dict):
        cls.product_list.append(dict)
        return 1
    @classmethod
    def update(cls,dict):
        for item in cls.product_list:
            if item['id']==id:
                item.insert(dict)
                return item
    @classmethod
    def find_by_id(cls,id:int):
        #for item in cls.product_list:
            #if item['id']== id :
                #return item
        next(item for item in cls.product_list if item['id']==id)
    @classmethod
    def remove(cls,dict):
        for item in cls.product_list:
            if item['id']==id:
                dict.remove(item)


