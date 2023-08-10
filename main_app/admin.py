from django.contrib import admin
from .models import Address
from .models import Profile

admin.site.register(Profile)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass