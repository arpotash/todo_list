from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import NoteUser


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(NoteUser, CustomUserAdmin)