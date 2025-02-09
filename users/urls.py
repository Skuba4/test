from django.urls import path
from . import views

app_name = 'users'
def func_test():
        pass


urlpatterns = [
        path('', views.Home.as_view(), name='home'),
]