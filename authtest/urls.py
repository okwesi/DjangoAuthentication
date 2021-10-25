from django.conf.urls import url,include
from .import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('signup/', views.signup, name='signup'),
    url('secret/', views.secret_page, name='secret_page'),
    url('secret2/', views.SecretPage.as_view(), name='secret_page2'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('allauth.urls')),

]