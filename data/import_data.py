import xlrd
import django
import os
import sys


def get_run_env():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BMS.settings")
    django.setup()
    return base_path


def import_data(path):
    from index.models import GZLM
    for file in os.listdir(path):
        if file.endswith('.xlsx'):
            file_name = os.path.join(path, file)
            print(f"正在读取文件：{file_name}")
            data = xlrd.open_workbook(file_name)
            table = data.sheet_by_index(0)
            table_rows = table.nrows

            write_count = 0
            for rowNum in range(table_rows):
                #  去掉表头, 表尾汉字
                if 1 < rowNum < table_rows - 1:
                    if not any(table.row_values(rowNum)[1: 17]):
                        continue

                    gzlm_instances = GZLM(
                        company_name=table.row_values(rowNum)[1],
                        date=table.row_values(rowNum)[2],
                        number_plate=table.row_values(rowNum)[3],
                        driver=table.row_values(rowNum)[4],
                        id_card1=table.row_values(rowNum)[5],
                        contact_detail1=table.row_values(rowNum)[6],
                        driver2=table.row_values(rowNum)[7],
                        id_card2=table.row_values(rowNum)[8],
                        contact_detail2=table.row_values(rowNum)[9],
                        issued_area=table.row_values(rowNum)[10],
                        arrival_area=table.row_values(rowNum)[11],
                        arrival_time=table.row_values(rowNum)[12],
                        leave_time=table.row_values(rowNum)[13],
                        status=table.row_values(rowNum)[14],
                        car_attribution=table.row_values(rowNum)[15],
                        remark=table.row_values(rowNum)[16],
                    )
                    gzlm_instances.save()
                    write_count += 1
            print(f"读取文件：{file_name}, 共写入数据 {write_count} 条")


if __name__ == '__main__':
    path = get_run_env()
    import_data(os.path.join(path, "data"))
    print('写入完成!')
