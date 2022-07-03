from django.urls import path

from works.views import WorksView

app_name = 'works'
urlpatterns = [
    path('', WorksView.as_view(), name='works')
]