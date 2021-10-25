from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.core.mail import send_mail
# https://docs.djangoproject.com/en/3.2/topics/auth/default/
# default link to learn about about the authorization in django
# https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
# link to0 blog post about editing the forms templates provided by django


#username: user
#password: konkonsapolice@123


def home(request):
    # function for the home html page
    count = User.objects.count()
    return render(request, 'home.html', {
        'no_of_users':count
    })


def signup(request):
    # for the signup button in the sign up html page
    if request .method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
            'form' : form
        })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin,TemplateView):
    template_name = "secret_page2.html"