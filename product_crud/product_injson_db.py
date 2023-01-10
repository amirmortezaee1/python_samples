<<<<<<< HEAD
import json

class JsonDict:

    def __init__(self, file_path):
        
        self.file_path = file_path

    def add(self,dict):
        with open (self.file_path, 'r') as f :
            items=list(json.load(f))
            items.append(dict)
    
        with open(self.file_path, 'w') as f:
            json.dump(items,f)


    def update(self,dict,id:int):
        with open (self.file_path,'r') as f:
            items=list(json.load(f))
            for item in items:
                if item['id'] == id:
                    items.remove(item)
                    items.append(dict)
                    
        with open (self.file_path, 'w') as f:
            json.dump(items,f)

    def read(self):
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

    def remove(self,id:int):
        with open (self.file_path, 'r') as f:
            items=list(json.load(f))
            for item in items :
                if item['id']== id:
                    items.remove(item)

        with open(self.file_path,'w') as f:
            json.dump(items,f)
=======

>>>>>>> main
