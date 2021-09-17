from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.Upload.as_view(), name="upload")
]
