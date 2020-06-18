

from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from adminapp.views import *
# admin.site.site_header = 'hghg'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',Signupview.as_view()),

    path('', TemplateView.as_view(template_name="index.html")),
    path('auth/', include('adminapp.urls')),
    
    

   
    # path('logout/',TemplateView.as_view(template_name = 'recruitment/mrf/login.html'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)