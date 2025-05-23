from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("best_model.pkl")

# สร้าง FastAPI app
app = FastAPI()

# สร้าง schema ของ input data (ต้องตรงกับฟีเจอร์ที่ใช้ train)
class LoanInput(BaseModel):
    SEX: int
    NO_OF_DEPENDENT: int
    MARITAL_STATUS: int
    YRS_IN_PRESENT_JOB: int
    AGE: int
    EDUCATION: int
    YEARS_OF_EXPERIENCE: int
    TOTAL_MONTHLY_INCOME: float
    LOAN_AMOUNT: float
    COMPANY_TYPE: int

@app.get("/")
def root():
    return {"message": "Loan Risk Prediction API Ready!"}

@app.post("/predict")
def predict(data: LoanInput):
    input_data = np.array([[v for v in data.dict().values()]])
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
