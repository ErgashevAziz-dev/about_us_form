from django.urls import path

from .views import main, person_list, view
urlpatterns = [
    path('register/', main, name='main'),
    path('people/', person_list, name='people_list'),
    path('', view, name='view'),
]