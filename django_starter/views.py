from django.contrib.auth import login
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from {{project_name}}.forms import RegistrationForm


def index(request):
    return TemplateResponse(request, 'index.html', {})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return TemplateResponse(request, 'registration/register.html', {
        'form': form
    })
