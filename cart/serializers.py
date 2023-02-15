from rest_framework import serializers
from .models import User, Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'title', 'price', 'description', 'image', 'quantity')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'chat_id')

class GetTitleCart(serializers.ModelSerializer):
    class Meta: 
        model = Cart
        fields = ('title',)

class GetUserSerializer(serializers.ModelSerializer):
    cart = GetTitleCart(many = True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'chat_id', 'cart')