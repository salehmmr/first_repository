from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
@permission_classes(())
def registration(request):
    if request.method == 'POST':
        data = request.data
        data_email = data['email']
        data_username = data['username']
        data_password = data['password']
        data_password2 = data['password2']
        if not models.user.objects.filter(username=data_username).exists():
            if data_password == data_password2:
                new_user = models.user.objects.create(username=data_username, password=data_password, email=data_email)
                return Response({"message": "Created Successfully!"})
            return Response({"message": "Passwords not matched!"})
        return Response({"message": "Username already exists!"})