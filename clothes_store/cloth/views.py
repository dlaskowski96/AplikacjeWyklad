from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import cloth,Client
from .serializers import clothSerializer, ClientSerializer,
from rest_framework import permissions
from django.contrib.auth.models import User

class clothList(generics.ListCreateAPIView):
    queryset = cloth.objects.all()
    serializer_class = clothSerializer
    name = 'cloth'
    filterset_fields = ['name','date of purchase','brand of clothes']
    search_fields = ['name']
    ordering_fields = ['date of purchase','brand of clothes']

class ClientList(generics.ListCreateAPIView):
        queryset = Client.objects.all()
        serializer_class = clothSerializer
        name = 'Client'
        filterset_fields = ['Name', 'Surname', 'address','date of purchase']
        search_fields = ['Name']
        ordering_fields = ['date of purchase','Surname','address','date of purchase']


class clothDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cloth.objects.all()
    serializer_class = clothSerializer
    name = 'cloth-detail'

class clothDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Client.objects.all()
        serializer_class = ClientSerializer
        name = 'cloth-detail'



class cloth(generics.ListCreateAPIView):
    queryset = cloth.objects.all()
    serializer_class = cloth
    name = 'cloth-list'
    filter_fields = ['name', 'date of purchase', 'brand of clothes']
    search_fields = ['name']
    ordering_fields = ['name', 'date of purchase', 'brand of clothes']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Client(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = cloth
    name = 'Cient-list'
    filter_fields = ['Name', 'Surname', 'address','date of purchase']
    search_fields = ['Name']
    ordering_fields = ['Name', 'Surname', 'address','date of purchase']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class clothDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cloth.objects.all()
    serializer_class = clothSerializer
    name = 'cloth-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'Client-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class clothList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'cloth-list'
    ordering_fields = ['name','date of purchase', 'brand of clothes']

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    ordering_fields = ['Name', 'Surname','address','date of purchase']


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cloth': reverse(clothList.name, request=request),
                         'Client': reverse(Client.name, request=request),
                         'users': reverse(UserList.name, request=request)
})