# pip install xlwt
import xlwt
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def excel_file(request):
    response = HttpResponse(content_type='application/ms-excel')
    filename = 'excel_file.xls'
    # content = "inline; filename=%s" % filename
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write_merge(0, 0, 0, 3, 'User Record', font_style)

    columns = ['S No.', 'Username', 'First name', 'Last name', 'Email address', 'Last login']
    row_num = 2
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    float_font_style = xlwt.Style.easyxf(num_format_str="#.00")

    '''For Date and Time use strfime()'''
    rows = User.objects.all()
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, float(row_num - 2), float_font_style)
        ws.write(row_num, 1, row.username, font_style)
        ws.write(row_num, 2, row.first_name, font_style)
        ws.write(row_num, 3, row.last_name, font_style)
        ws.write(row_num, 4, row.email, font_style)
        ws.write(row_num, 5, row.last_login.strftime('%Y-%m-%d'), font_style)

    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for row in rows:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
