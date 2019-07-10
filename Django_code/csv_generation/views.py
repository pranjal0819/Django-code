import csv

from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def csv_file(request):
    response = HttpResponse(content_type='text/csv')
    filename = 'csv_file.csv'
    # content = "inline; filename=%s" % filename
    content = "attachment; filename=%s" % filename
    response['Content-Disposition'] = content

    writer = csv.writer(response)
    ''' Generate csv file for User model'''
    writer.writerow(['Username', 'First name', 'Last name', 'Email address', 'Last login'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email', 'last_login')
    for user in users:
        writer.writerow(user)
    return response
