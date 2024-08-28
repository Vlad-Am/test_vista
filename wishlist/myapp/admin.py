from django.contrib import admin

from .models import MyWishList


@admin.register(MyWishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'url', 'description')
    search_fields = ('name',)
