from django.db import models

class PredictionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    SEX = models.IntegerField()
    NO_OF_DEPENDENT = models.IntegerField()
    MARITAL_STATUS = models.IntegerField()
    YRS_IN_PRESENT_JOB = models.FloatField()
    AGE = models.IntegerField()
    EDUCATION = models.IntegerField()
    YEARS_OF_EXPERIENCE = models.IntegerField()
    TOTAL_MONTHLY_INCOME = models.IntegerField()
    LOAN_AMOUNT = models.FloatField()
    COMPANY_TYPE = models.FloatField()
   





