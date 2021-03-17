from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from factory_app.models import TableLeg, Table, Leg, Feet
from factory_app.serializers import  TableLegSerializer, TableSerializer, LegSerializer, FeetSerializer

# Create your views here.
# Upon visiting the home page the the default basic urls for corresponding views via DefaultRouter will be presented.

class TableViewSet(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Table.objects.all(), 'serializer_class': TableSerializer},
        {'queryset': TableLeg.objects.all(), 'serializer_class': TableLegSerializer},
    ]

class LegModelViewSet(ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer


class FeetModelViewSet(ModelViewSet):
    queryset = Feet.objects.all()
    serializer_class = FeetSerializer
