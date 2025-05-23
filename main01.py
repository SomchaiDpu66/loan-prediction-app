from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# โหลดโมเดลและ scaler
model = joblib.load("decision_tree_model.pkl")
scaler = joblib.load("scaler.pkl")


@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/", response_class=HTMLResponse)
async def predict_form(
    request: Request,
    AGE: float = Form(...),
    INCOME: float = Form(...),
    GENDER: int = Form(...),
    EDUCATION: int = Form(...),
    MARRIED: int = Form(...),
    JOB: int = Form(...),
    SCORE: float = Form(...),
    ONLINE: int = Form(...)
):
    try:
        # จัดเรียงข้อมูลตามลำดับที่ใช้ train
        input_data = np.array(
            [[AGE, INCOME, GENDER, EDUCATION, MARRIED, JOB, SCORE, ONLINE]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][1]
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": {
                "prediction": int(prediction),
                "probability": round(float(prob), 4)
            }
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": {"error": str(e)}
        })
