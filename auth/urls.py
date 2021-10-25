
from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    url('authtest/', include("authtest.urls")),
    url('admin/', admin.site.urls),
]
