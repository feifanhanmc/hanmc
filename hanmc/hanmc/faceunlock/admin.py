from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Account Info',     {'fields':['account', 'nickname','email', 'has_faceset']}),
    ]
    search_fields = ['account', 'nickname']
    list_display = ['account', 'nickname','has_faceset']
    list_filter = ['modify_time']
    
admin.site.register(User, UserAdmin)