from rest_framework import serializers

from .models import MyWishList


class MyWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWishList
        fields = ('id', 'name', 'price', 'url', 'description')
