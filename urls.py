from django.urls import path
from myapp import views

urlpatterns = [
    path('lorenz/', views.lorenz, name='lorenz'),
]
