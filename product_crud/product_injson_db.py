import json

class JsonDict:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_dict_to_json_file(self,dict):
        
            
            with open(self.file_path, 'r') as f:
                exiting_data={}

            exiting_data.update(dict)


            with open(self.file_path, 'w') as f:
                json.dump(dict, f)