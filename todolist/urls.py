from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('all', views.all, name="index"),
    path('specific/<int:pk>', views.specific),
]

urlpatterns = format_suffix_patterns(urlpatterns)