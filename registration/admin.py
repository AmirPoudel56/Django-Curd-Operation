from django.contrib import admin

from registration.models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'gender',
        'email',
        'phone_number',
    )
