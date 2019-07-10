# pip install xhtml2pdf
from io import BytesIO

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
def pdf_file(request):
    users = User.objects.all()
    context = {'user_list': users}
    # return render(request, self.template_name, context)
    template = get_template('pdf_file.html')
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        filename = "pdf_file.pdf"
        # content = "inline; filename=%s" % filename
        content = "attachment; filename=%s" % filename
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Error")
