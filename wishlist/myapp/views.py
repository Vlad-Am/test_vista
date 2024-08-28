from rest_framework import viewsets

from .models import MyWishList
from .serializers import MyWishListSerializer


class MyWishListView(viewsets.ModelViewSet):
    queryset = MyWishList.objects.all()
    serializer_class = MyWishListSerializer
