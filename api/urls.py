from django.urls import path
from .views import *

urlpatterns = [
    path("cars/", CarView.as_view()),
    path("cars/<int:id>", CarView.as_view()),
]
