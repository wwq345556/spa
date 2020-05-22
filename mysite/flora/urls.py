from django.urls import path
from . import views
urlpatterns = [
    path('flora/',views.hello),
    path('orm/',views.orm),
    path('list/',views.flora_list),
    path('add/',views.flora_add),
    path('delete/',views.flora_delete),
    path('update/',views.flora_update),
    path('info/',views.flora_info)
]