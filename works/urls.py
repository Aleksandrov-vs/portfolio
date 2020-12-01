from django.urls import path, include
from django.conf.urls import url
from .views import WorksApiView

urlpatterns = [
    path('', WorksApiView.as_view(), name='view_all_works')
]