from django.urls import path
from . import views

app_name = 'malema'

urlpatterns = [
    path('biography/', views.biography, name='biography'),
    path('life_education/', views.life_education, name='life_education'),
    path('anc_youth/', views.anc_youth, name='anc_youth'),

]