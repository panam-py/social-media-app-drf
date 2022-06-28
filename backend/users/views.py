from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import User
from .serializers import UserSerializer

class UserCreateListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

