from django.shortcuts import render
from .models import Cliente
from .sirializers import ClienteSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from core.permissions import IsAdmin, IsUserPro, IsUserDefault, IsAdminOrUserPro

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAdminOrUserPro]
    
    
    
# Create your views here.
