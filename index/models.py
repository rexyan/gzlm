from django.db import models


# Create your models here.
class GZLM(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    company_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    id_card1 = models.CharField(max_length=100)
    contact_detail1 = models.CharField(max_length=100)
    driver2 = models.CharField(max_length=100)
    id_card2 = models.CharField(max_length=100)
    contact_detail2 = models.CharField(max_length=100)
    issued_area = models.CharField(max_length=100)
    arrival_area = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    leave_time = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    car_attribution = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)



