from django.urls import path

from main.views import HomeView, ContactView

app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact')
]