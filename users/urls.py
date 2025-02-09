from django.urls import path
from . import views

app_name = 'users'
def func_test():
        pass

def func_test_1():
        pass


urlpatterns = [
        path('', views.Home.as_view(), name='home'),
]