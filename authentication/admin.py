# # # authentication/admin.py
# # from django.contrib import admin
# # from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# # from .models import User

# # class CustomUserAdmin(BaseUserAdmin):
# #     list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_verified', 'is_staff', 'is_superuser', 'is_active')
# #     search_fields = ('email', 'first_name', 'last_name', 'phone_number')
# #     list_filter = ('is_staff', 'is_superuser', 'is_active')
# #     ordering = ('email',)

# # admin.site.register(User, CustomUserAdmin)

# # authentication/admin.py
# from django.contrib import admin
# # from django.contrib.auth.admin import UserAdmin
# from .models import User

# # class CustomUserAdmin(UserAdmin):
# #     model = User
# #     list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_verified', 'is_active', 'is_staff', 'is_superuser']
# #     search_fields = ['email', 'first_name', 'last_name', 'phone_number']
# #     list_filter = ['is_verified', 'is_active', 'is_staff', 'is_superuser']

# admin.site.register(User)


# # authentication/admin.py
# from django.contrib import admin
# from .models import User


# admin.site.register(User)


# authentication/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_verified', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']
    list_filter = ['is_verified', 'is_active', 'is_staff', 'is_superuser']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)

