from rest_framework import routers

from .apps import MyappConfig
from .views import MyWishListView

name = MyappConfig.name

router = routers.DefaultRouter()
router.register(r"MyWishList", MyWishListView, basename="MyWishList")

urlpatterns = [

              ] + router.urls
