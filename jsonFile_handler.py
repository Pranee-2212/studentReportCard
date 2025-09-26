import json 

def save_as_json(student):
     try:
          file_name="data.json"
          with open(file_name, "w") as file:
               json.dump(student, file)
               print("successfully saved")
     except Exception as e:
          print("Error in Saving the file")

def load_from_json():
     try:
          file_name="data.json"
          with open(file_name, "r") as file:
               data=json.load(file)
               data=dict(data)
          return data
     except Exception as e:
          print("error in reading File")

