import json

class JsonDict:
    product_list_json=[]

    def __init__(self, file_path):
        self.file_path = file_path


    def add_dict_to_json_file(self,dict):
        self.product_list_json.append(dict)

        with open(self.file_path, 'w') as f:
            json.dump(self.product_list_json,f)


    def update_json(self,dict,id:int):
        with open (self.file_path,'r') as f:
            items=list(json.load(f))
            for item in items:
                if item['id'] == id:
                    items.remove(item)
                    items.append(dict)
                    
        with open (self.file_path, 'w') as f:
            json.dump(items,f)

    def read_json(self):
        with open (self.file_path,'r') as f :
            items=json.load(f)
            for item in items :
                return item

    def find_by_id(self,id:int):
        with open(self.file_path, 'r') as f:
            items=json.load(f)
            for item in items :
                if item['id']== id:
                    return item

    def delete_json(self,id:int):
        with open (self.file_path, 'r') as f:
            items=list(json.load(f))
            for item in items :
                if item['id']== id:
                    items.remove(item)

        with open(self.file_path,'w') as f:
            json.dump(items,f)