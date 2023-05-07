from django.contrib import admin
from .models import User,AuctionList
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email", "password")

class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id","username","title","description","current_price","photo","categories")

admin.site.register(User, UserAdmin)
admin.site.register(AuctionList, AuctionAdmin)