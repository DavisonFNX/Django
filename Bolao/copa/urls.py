from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

  url('^', include('django.contrib.auth.urls')),
  url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='bolao/login.html')),
  url(r'^bolao/', include('bolao.urls')),
  url(r'^admin/', admin.site.urls),

]