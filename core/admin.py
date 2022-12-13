from django.contrib import admin
from core.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)