from django.contrib import admin
from .models import GZLM


class GZLMAdmin(admin.ModelAdmin):
    # 可编辑
    list_display = (
        'id', 'company_name', 'date', 'number_plate', 'driver', 'id_card1', 'contact_detail1', 'driver2', 'id_card2',
        'contact_detail2', 'issued_area', 'arrival_area', 'arrival_time', 'leave_time', 'status', 'car_attribution',
        'remark'
    )

    # list_editable = list_display
    search_fields = list_display

    # 设置点击哪些字段可以点击进入编辑界面，默认为id字段
    list_display_links = list_display

    # 分页，每页显示条数
    list_per_page = 20


admin.site.register(GZLM, GZLMAdmin)
admin.site.site_header = '贵州快递物流集聚区管理委员会统计系统'
