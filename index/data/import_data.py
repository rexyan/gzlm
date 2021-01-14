import xlrd


def import_data(file_path):
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_index(0)
    table_nrows = table.nrows

    for rowNum in range(table_nrows):
        #  去掉表头, 表尾汉字
        if 1 < rowNum < table_nrows - 1:
            print(table.row_values(rowNum))


if __name__ == '__main__':
    import_data('data.xlsx')
