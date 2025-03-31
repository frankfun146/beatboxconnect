from django.urls import path, include
from .views import tutorials, tutorial_detail


urlpatterns = [
    path('', tutorials, name='tutorials'),
    path('<str:sound_name>/', tutorial_detail, name='tutorial_detail'),
]
