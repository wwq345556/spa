from django.urls import path
from . import views
urlpatterns = [
    # path('list/',views.flora_list),
    path('add/',views.plants_add),
    # path('delete/',views.flora_delete),
    # path('update/',views.flora_update),
    # path('info/',views.flora_info)
]