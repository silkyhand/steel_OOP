from django.contrib import admin
from django.contrib.auth import get_user_model

from .forms import CreationForm, ChangeForm


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = User
    list_display = ('email', 'username', 'user_discount', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    list_editable = ('user_discount',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'user_discount',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin,)
