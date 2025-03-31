from django.urls import path
from .views import home, contact_success, contact


urlpatterns = [
    path('', home, name='main_home'),
    path('contact/', contact, name='contact'),
    path('contactsuccess/', contact_success, name='contact_success'),

]
