from django.contrib import admin
from django.urls import path

from csv_generation.views import csv_file
from excel_generation.views import excel_file
from pdf_generation.views import pdf_file
from .views import home
from email_sending.views import send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('csv-file/', csv_file, name='csv_file'),
    path('excel-file/', excel_file, name='excel_file'),
    path('pdf-file', pdf_file, name='pdf_file'),
    path('send-mail',send_email, name='send_email'),
]
