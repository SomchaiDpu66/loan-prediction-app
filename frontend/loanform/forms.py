from django import forms

class LoanInputForm(forms.Form):
    SEX = forms.IntegerField(label='Sex (0=Male, 1=Female)', min_value=0)
    NO_OF_DEPENDENT = forms.IntegerField(label='Number of Dependents', min_value=0)
    MARITAL_STATUS = forms.IntegerField(label='Marital Status (e.g., 0=Single, 1=Married, 2=Divorced)', min_value=0)
    YRS_IN_PRESENT_JOB = forms.IntegerField(label='Years in Present Job', min_value=0)
    AGE = forms.IntegerField(label='Age', min_value=0)
    EDUCATION = forms.IntegerField(label='Education Level (e.g., 0=High School, 1=Bachelor, etc.)', min_value=0)
    YEARS_OF_EXPERIENCE = forms.IntegerField(label='Years of Experience', min_value=0)
    TOTAL_MONTHLY_INCOME = forms.FloatField(label='Total Monthly Income', min_value=0)
    LOAN_AMOUNT = forms.FloatField(label='Loan Amount', min_value=0)
    COMPANY_TYPE = forms.IntegerField(label='Company Type (e.g., 0=Government, 1=Private, etc.)', min_value=0)
