from django.contrib import admin
from .models import User,AuctionList,Comments
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email", "password")

class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id","username","title","description","current_price","photo","categories")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id","username","product","text","timestamp")
admin.site.register(User, UserAdmin)
admin.site.register(AuctionList, AuctionAdmin)
admin.site.register(Comments,CommentsAdmin)