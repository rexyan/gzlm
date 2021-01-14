from django.db import models


# Create your models here.
class GZLM(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name="id")
    company_name = models.CharField(max_length=100, verbose_name="企业名称", null=True)
    date = models.CharField(max_length=100, verbose_name="日期", null=True)
    number_plate = models.CharField(max_length=100, verbose_name="车牌号", null=True)
    driver = models.CharField(max_length=100, verbose_name="驾驶人", null=True)
    id_card1 = models.CharField(max_length=100, verbose_name="身份证号", null=True)
    contact_detail1 = models.CharField(max_length=100, verbose_name="联系方式", null=True)
    driver2 = models.CharField(max_length=100, verbose_name="驾乘人员", null=True)
    id_card2 = models.CharField(max_length=100, verbose_name="身份证号", null=True)
    contact_detail2 = models.CharField(max_length=100, verbose_name="联系方式", null=True)
    issued_area = models.CharField(max_length=100, verbose_name="发出地区", null=True)
    arrival_area = models.CharField(max_length=100, verbose_name="到达地区", null=True)
    arrival_time = models.CharField(max_length=100, verbose_name="到达企业时间", null=True)
    leave_time = models.CharField(max_length=100, verbose_name="离开企业时间", null=True)
    status = models.CharField(max_length=100, verbose_name="完成状态", null=True)
    car_attribution = models.CharField(max_length=100, verbose_name="车辆归属", null=True)
    remark = models.CharField(max_length=100, verbose_name="备注", null=True)

    class Meta:
        verbose_name_plural = "车辆到达数据"
