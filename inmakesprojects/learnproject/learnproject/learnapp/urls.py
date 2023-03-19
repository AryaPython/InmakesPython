from . import views
from django.urls import path


urlpatterns = [
            path('',views.forest,name="forest")
]