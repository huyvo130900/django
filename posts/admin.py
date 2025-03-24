from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'vai_tro', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('vai_tro', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Quyền', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Thông tin khác', {'fields': ('vai_tro',)}),  # Đảm bảo 'vai_tro' có ở đây
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'vai_tro', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('username',)  # Có thể đổi về 'email' nếu bạn thích

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
