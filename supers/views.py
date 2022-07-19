from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from .serializers import SuperSerializer
from .models import Super
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def super_methods(request):
  if request.method == 'GET':
    supers_all = Super.objects.all()
    serializer = SuperSerializer(supers_all, many = True)
    return Response(serializer.data)

  elif request.method =='POST':
    serializer = SuperSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def super_by_id(request,pk):
  supers = get_object_or_404(Super, pk=pk)
  if request.method == 'GET':
    serializer = SuperSerializer(supers)
    return Response(serializer.data)
  elif request.method =='PUT':
    serializer = SuperSerializer(supers, data=request.data, )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
