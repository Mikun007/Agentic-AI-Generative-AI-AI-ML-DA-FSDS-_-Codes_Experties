from fastapi import FastAPI
import json
app = FastAPI()

#lets create helper function to read ptient records from a file
def load_data():
      with open("patient.json", "r") as f:
            data = json.load(f)
      return data

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/mikun_das")
def mikun_das():
    return {"message": "This is a FastAPI application created by Mikun Das"}

@app.get("/patient_record")
def patient_record():
      return {"message": "This is a FastAPI application to manage patient records."}


@app.get("/view")
def view():
      data = load_data()
      return data