from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from factory_app.models import TableLeg, Table, Leg, Feet
from factory_app.serializers import  TableLegSerializer, TableSerializer, LegSerializer, FeetSerializer

# Create your views here.
# Upon visiting the home page the the default basic urls for corresponding views via DefaultRouter will be presented.

class TableLegModelViewSet(ModelViewSet):
    queryset = TableLeg.objects.all()
    serializer_class = TableLegSerializer


class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class LegModelViewSet(ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer


class FeetModelViewSet(ModelViewSet):
    queryset = Feet.objects.all()
    serializer_class = FeetSerializer
