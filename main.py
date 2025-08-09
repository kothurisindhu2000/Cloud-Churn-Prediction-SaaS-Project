from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Churn Prediction API!"}

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    # Read uploaded file as pandas dataframe
    df = pd.read_csv(file.file)
    
    # Get number of rows and columns in uploaded file
    rows, cols = df.shape
    
    return {"filename": file.filename, "rows": rows, "columns": cols}
