from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapeCRUD.models import Triangle,Rectangle,Square,Diamond
from shapeCRUD.serializers import TriangleSerializer, RectangleSerializer,SquareSerializer,DiamondSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from shapeCRUD.permissions import IsOwnerOrReadOnly

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


@api_view(['GET', 'POST'])
def shape_list(request,shape):
    """
    List all code shapeCRUD, or create a new shape.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    shapeDict = {'triangle': Triangle, 'square': Square, 'diamond': Diamond, 'rectangle': Rectangle}
    serialDict = {'triangle': TriangleSerializer, 'square': SquareSerializer, 'diamond': DiamondSerializer, 'rectangle': RectangleSerializer}
    _shape = shapeDict[shape]
    _serializer = serialDict[shape]
    if request.method == 'GET':
        shapeCRUD = _shape.objects.all()
        serializer = _serializer(shapeCRUD, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = _serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print('Serializer is valid')
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def shape_detail(request,shape, pk):
    """
    Retrieve, update or delete a shape.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    shapeDict = {'triangle': Triangle, 'square': Square, 'diamond': Diamond, 'rectangle': Rectangle}
    serialDict = {'triangle': TriangleSerializer, 'square': SquareSerializer, 'diamond': DiamondSerializer, 'rectangle': RectangleSerializer}
    _shape = shapeDict[shape]
    _serializer = serialDict[shape]

    try:
        shape = _shape.objects.get(pk=pk)
    except _shape.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = _serializer(shape)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = _serializer(shape, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shape.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_area(request,shape,pk):
    shapeDict = {'triangle': Triangle, 'square': Square, 'diamond': Diamond, 'rectangle': Rectangle}
    _shape = shapeDict[shape]
    try:
        shape = _shape.objects.get(pk=pk)
    except _shape.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response({'Area':shape.area()})

@api_view(['GET'])
def get_perimeter(request,shape,pk):
    shapeDict={'triangle':Triangle,'square':Square,'diamond':Diamond,'rectangle':Rectangle}
    _shape=shapeDict[shape]
    try:
        shape = _shape.objects.get(pk=pk)
    except _shape.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response({'Perimeter':shape.perimeter()})

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users')
    else:
        form = UserCreationForm()
    return render(request, 'shapeCRUD/signup.html', {'form': form})