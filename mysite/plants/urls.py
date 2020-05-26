from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.plants_list),
    path('add/',views.plants_add),
    path('delete/',views.plants_delete),
    path('update/',views.plants_update),
    path('info/',views.plants_info)
]