from django.urls import path
from . import views
urlpatterns = [
    path('flora/',views.hello),
    path('orm/',views.orm),
    path('list/',views.flora_list)
]