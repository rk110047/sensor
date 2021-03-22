from django.shortcuts import render
from .serializers import ActivitySerializer
from rest_framework import generics
from .models import Activity
# Create your views here.



class ActivityListCreateAPIView(generics.ListCreateAPIView):
	serializer_class 	=	ActivitySerializer
	queryset 			=	Activity.objects.all()


class ActivityRetrieveUpdateDestroyAPIVIew(generics.RetrieveUpdateDestroyAPIView):
	serializer_class 	=	ActivitySerializer
	queryset 			=	Activity.objects.all()
	lookup_field 		=	"id"