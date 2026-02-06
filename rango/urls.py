from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Add this new pattern for the category detail page
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
]