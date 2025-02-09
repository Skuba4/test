from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'users/home.html'


class Name_1:
    pass