from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')  # Fields to display in the list view
    search_fields = ('first_name', 'last_name', 'email','phone_number')  # Fields to search by

admin.site.register(Contact, ContactAdmin)
