from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CartSerializer, GetUserSerializer
from .models import User, Cart


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method in ('GET', 'HEAD', 'OPTIONS'):
            return GetUserSerializer
        return UserSerializer


class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   