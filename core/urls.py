from django.urls import path
from core.views import home,save_data,delete,edit


urlpatterns = [

    path("",home,name="home"),
    path("save/",save_data,name='save'),
    path("delete/",delete,name="delete"),
    path('edit/',edit,name="edit"),
]