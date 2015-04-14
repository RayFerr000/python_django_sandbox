from django.contrib import admin
from django.contrib.auth.models import Permission
from User.models import User

# Register your models here.

def make_staff(UserAdmin, request, queryset):
	#print queryset[0].is_staff
	queryset.update(is_staff = True)
	#print queryset[0].is_staff
class UserAdmin(admin.ModelAdmin):

    list_display = ('fname', 'lname', 'email', 'is_staff')

    search_fields =['email']
    actions = [make_staff]

    

admin.site.register(User, UserAdmin)

