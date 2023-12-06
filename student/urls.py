from django.urls import path
from . import views
urlpatterns = [
    path('name/',  views.sname, name='hello'),
    path('no/',  views.sno, name='main'),
]