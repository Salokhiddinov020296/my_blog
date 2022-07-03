from django.urls import path

from blogs.views import BlogsView

app_name = 'blogs'

urlpatterns = [
    path('', BlogsView.as_view(), name='blogs')
]