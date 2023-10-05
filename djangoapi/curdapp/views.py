from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users
from .serializers import usersserializer

@api_view(['GET'])
def UserView(request):
    api_urls = {
            'all_users': '/',
            'add': '/create',
            'update': '/update/pk',
            'delete': '/users/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def Addusers(request):
    user = usersserializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data)
    
@api_view(['GET'])
def Readusers(request):
    getusers = users.objects.all()

    if getusers:
        serializer = usersserializer(getusers, many=True)
        return Response(serializer.data)   

@api_view(['GET'])
def Readuser(request, pk):
    getuser = users.objects.get(pk=pk)
    userdata = usersserializer(getuser)
    return Response(userdata.data)
    
@api_view(['PUT'])
def Updateusers(request, pk):
    getuser = users.objects.get(pk=pk)
    data = usersserializer(instance=getuser, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)

@api_view(['DELETE'])
def Deleteusers(request, pk):
    getuser = users.objects.get(pk=pk)
    getuser.delete()
    return Response('deleted user')
