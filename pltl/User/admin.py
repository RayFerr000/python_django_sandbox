from django.contrib import admin
from User.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ('fname', 'lname', 'email')
    class Meta:
    	permissions = ()

admin.site.register(User, UserAdmin)
