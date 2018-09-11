from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import timezone
from django.forms.models import model_to_dict
import datetime


from render_application.forms import ApplicationForm

import pydf

months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}
# Create your views here.


def render_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            context = model_to_dict(model_instance, fields=[field.name for field in model_instance._meta.fields])
            now = datetime.datetime.now()
            context["reason"] = context["reason"].lower()
            context["year"] = now.year
            context["day"] = now.day
            context["month"] = months[now.month]
            html_string = render_to_string('stud_application.html', context)
            pdf = pydf.generate_pdf(html_string)

            return HttpResponse(pdf, content_type='application/pdf')
    else:
        form = ApplicationForm()
    return render(request, 'home.html', {'form': form})
