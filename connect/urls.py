from django.urls import path
from .views import signup_view, login_view, connect_home, logout_view, ask_question, answer_question, search_view

urlpatterns = [
    path('', connect_home, name='connect_home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ask/', ask_question, name='ask_question'),
    path('answer/<int:question_id>/', answer_question, name='answer_question'),
    path('search/', search_view, name='search'),
]
