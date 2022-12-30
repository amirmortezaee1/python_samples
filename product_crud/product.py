from datetime import datetime

class Product():

    _product_list = []
    

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.id = None
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt
       

    def create(self, id:int):
        self.id = id
        product = {'id': self.id, 'product':self}
        self._product_list.append(product)
        return self.__repr__()

    
    
    @classmethod
    def read(cls, id:int):
        for i in cls._product_list:
            if i['id'] == id:
                return i['product'].__repr__()
        return f"this id '{id}' does not exist"

    
    def update(self, new_attr):
        for key, value in new_attr.items():
            if key in self.__dict__:
                setattr(self, key, value) 
            
                 

    
    @classmethod
    def delete(cls, id):
        for i in cls._product_list:
            if i['id'] == id:
                cls._product_list.remove(i)
                return 'Done'


    @classmethod
    def list_all(cls):
        return tuple(cls._product_list)
    
    def __del__(self):
        pass


    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: N/A \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "
       