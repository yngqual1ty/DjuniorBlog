from django.contrib import admin
from .models import Publication, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser')

admin.site.register(User, UserAdmin)
admin.site.register(Publication)


