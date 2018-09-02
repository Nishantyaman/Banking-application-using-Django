from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.index,name='home'),
    path('ifsc/',views.bank_ifsc,name='ifsc'),
    path('name/',views.bank_name,name='name'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)