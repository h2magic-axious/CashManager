from django.urls import path

from Cash import views

app = 'Cash'
urlpatterns = [
    path('', views.index, name='index')
]
