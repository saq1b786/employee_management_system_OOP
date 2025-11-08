import json 

DATA_FILE = "employee_data.json"

def load_data():
  with open(DATA_FILE, 'r+') as file:
    json_file = file.read()
    if not json_file:
      return []
    else:
      data = json.loads(json_file) # converts JSON string to python dict
  return data

def save_data(data):
  add_data_to_json = json.dumps(data) # converts the python object back to json string
  with open(DATA_FILE, 'w') as file:
    file.write(add_data_to_json)