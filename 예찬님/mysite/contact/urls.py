from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.contact, name='contact'),
    # path('contact_complete/', views.contact_complete, name='contact_complete')
]