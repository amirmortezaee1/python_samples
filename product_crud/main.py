import datetime
from product import Product
from circle import Circle

def main():
    print('Hello World')

    mycircle = Circle(8)

    currentdatetime = datetime.datetime.utcnow()
    current_unixtimestamp = int(currentdatetime.timestamp())

    product_one = Product('Lenovo T410s',
        'Lenovo ThinkPad T410s Core i5 M560 2.66GHz 4GB RAM, WIN 10 14" AC ADAPTER',
        'The T410s provides a good companion for office use, that is well suited for business trips thanks to its 14.1 inch size and light weight.',
        'thinkbook-13x-gen-2-(13-inch-intel)',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/thinkbookx/thinkbook-13x-gen-2-(13-inch-intel)/21atcto1wwgb2?cid=gb:sem|se|google|G-UK-SEM-COMMERCIAL-PUBLIC-CCF-LF-Shopping-PLA-Brand-Commercial|Brand-CommercialLaptops-Intel',
        '21ATCTO1WWGB2',
        799.95,
        849.95,
        0,
        False,
        4,
        current_unixtimestamp,
        current_unixtimestamp,
        1)

    product_two = Product('Lenovo T530',
        'Lenovo 530',
        'some long descrition',
        'thinkbook-530',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530',
        'X394UB83NJ',
        689.95,
        549.95,
        0,
        False,
        8,
        current_unixtimestamp,
        current_unixtimestamp,
        1)

    x = ['Asus T410s',
        'Lenovo ThinkPad T410s Core i5 M560 2.66GHz 4GB RAM, WIN 10 14" AC ADAPTER',
        'The T410s provides a good companion for office use, that is well suited for business trips thanks to its 14.1 inch size and light weight.',
        'thinkbook-13x-gen-2-(13-inch-intel)',
        'https://www.lenovo.com/gb/en/p/laptops/thinkbook/thinkbookx/thinkbook-13x-gen-2-(13-inch-intel)/21atcto1wwgb2?cid=gb:sem|se|google|G-UK-SEM-COMMERCIAL-PUBLIC-CCF-LF-Shopping-PLA-Brand-Commercial|Brand-CommercialLaptops-Intel',
        '21ATCTO1WWGB2',
        799.95,
        849.95,
        0,
        False,
        4,
        current_unixtimestamp,
        current_unixtimestamp,
        1]

    # key = ["id" ,"category_id", "title", "short_description", "description", "slug", "permalink", "is_available", "sku", "price", "regular_price", "sale_price", 
        # "sale_price", "manage_stock", "is_available", "is_visible", "date_created_gmt", "date_modified_gmt"]
    update_items= {'id': '2', 'category_id': 14, 'title': 'Asus', 'short_description': 'Lenovo 530',
     'description': 'some long descrition', 'slug': 'thinkbook-530',
      'permalink': 'https://www.lenovo.com/gb/en/p/laptops/thinkbook/530', 'is_available': False, 'sku': 'X394UB83NJ'
      , 'price': 689.95, 'regular_price': 549.95, 'sale_price': 0, 'manage_stock': False, 'stock_quantity': 8,
       'is_visible': True, 'date_created_gmt': 1672646902, 'date_modified_gmt': 1672646902}

    # save items to a list of dictionary,(method input is id) 
    product_one.create("1")
    product_two.create("2")
  
    # delete instance of products 
    del product_one
    del product_two

    print("--------------------------------------")

    # read items by id method
    print(Product.read("2"))

    print("--------------------------------------")

    # delete items by id
    print(Product.delete("1"))

    print("--------------------------------------")

    # update method update(id, key, vallue)
    # give an id for find the item. and the key that we want to update 
    # value that change previous value to new one
    Product.update_one_item("2", "title",  "Asus")

    # thid class method give id for first argument
    # and for second argument give dictionary
    # this method update all items 
    Product.update_all_item("2", update_items)

    print("--------------------------------------")

    # list all of items
    print(Product.list_all())



if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()