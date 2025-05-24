from .models import PredictionLog
from django.shortcuts import render
from .forms import LoanForm
import requests

def loan_predict_view(request):
    result = None
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post("http://fastapi:8000/predict", json=data)
            result = response.json().get("prediction")

            # Save log
            PredictionLog.objects.create(
                SEX=data['SEX'],
                NO_OF_DEPENDENT=data['NOOFDEPENDENT'],
                MARITAL_STATUS=data['MARITALSTATUS'],
                YRS_IN_PRESENT_JOB=data['Year_JOB'],
                AGE=data['AGE'],
                EDUCATION=data['EDUCATION'],
                YEARS_OF_EXPERIENCE=data['YEARSEXPERIENCE'],
                TOTAL_MONTHLY_INCOME=data['TOTALINCOME'],
                LOAN_AMOUNT=data['LOANAMOUNT'],
                COMPANY_TYPE=data['COMPANYTYPE'],
                result=result



            )
    else:
        form = LoanForm()
    return render(request, 'form.html', {'form': form, 'result': result})

def dashboard_view(request):
    logs = PredictionLog.objects.all().order_by("-timestamp")[:100]
    return render(request, 'dashboard.html', {"logs": logs})
