from django.db import models


# Create your models here.
class GZLM(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True, verbose_name="id")
    company_name = models.CharField(max_length=100, verbose_name="企业名称")
    date = models.CharField(max_length=100, verbose_name="日期")
    number_plate = models.CharField(max_length=100, verbose_name="车牌号")
    driver = models.CharField(max_length=100, verbose_name="驾驶人")
    id_card1 = models.CharField(max_length=100, verbose_name="身份证号")
    contact_detail1 = models.CharField(max_length=100, verbose_name="联系方式")
    driver2 = models.CharField(max_length=100, verbose_name="驾乘人员")
    id_card2 = models.CharField(max_length=100, verbose_name="身份证号")
    contact_detail2 = models.CharField(max_length=100, verbose_name="联系方式")
    issued_area = models.CharField(max_length=100, verbose_name="发出地区")
    arrival_area = models.CharField(max_length=100, verbose_name="到达地区")
    arrival_time = models.CharField(max_length=100, verbose_name="到达企业时间")
    leave_time = models.CharField(max_length=100, verbose_name="离开企业时间")
    status = models.CharField(max_length=100, verbose_name="完成状态")
    car_attribution = models.CharField(max_length=100, verbose_name="车辆归属")
    remark = models.CharField(max_length=100, verbose_name="备注")

    class Meta:
        verbose_name_plural = "车辆到达数据"
