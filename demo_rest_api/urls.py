from django.urls import path
from . import views

urlpatterns = [
   path("", views.DemoRestApi.as_view(), name="demo_rest_api_resources_root"),
   path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources"),
   path("<str:id>/", views.DemoRestApiItem.as_view(), name="demo_rest_api_item"),
]