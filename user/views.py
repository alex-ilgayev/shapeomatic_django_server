from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from user.models import *
from user.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from datetime import date
from datetime import datetime
import re


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
