from django.urls import path
from .views import ActivityListCreateAPIView,ActivityRetrieveUpdateDestroyAPIVIew


app_name="activity"


urlpatterns =[
	path('LC/',ActivityListCreateAPIView.as_view(),name="lsit-create"),
	path('RUD/<id>/',ActivityRetrieveUpdateDestroyAPIVIew.as_view(),name="RUD")
]