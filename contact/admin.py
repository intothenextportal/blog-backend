from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'sent_at', 'read']
    list_filter = ['read', 'sent_at']
    readonly_fields = ['name', 'email', 'phone', 'message', 'sent_at']

    def has_add_permission(self, request):
        return False
