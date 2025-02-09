from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'users/home.html'


class Name_1:
    pass


class Name_2:
    """ИМИТИРУЮ ФИЧУ ДЛЯ ПРОВЕРКИ МАСТЕРОМ"""
    pass


class Name_3:
    """ДОБАВИЛ ДРУГОЙ ПОЛЬЗОВАТЕЛЬ"""
    pass
