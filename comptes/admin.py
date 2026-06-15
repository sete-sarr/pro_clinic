# from django.contrib import admin

# from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# from .models import User


# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User

#     list_display = ('email','prenom','nom','telephone','date_naissance', 'role', 'is_staff', 'is_active')
#     list_filter = ('role', 'is_staff', 'is_active')

#     ordering = ('email',)
#     search_fields = ('email',)

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Informations personnelles', {'fields': ('first_name', 'last_name', 'photo', 'bio')}),
#         ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_active', 'prenom', 'nom'),
#         }),
#     )

# # Register your models here.
