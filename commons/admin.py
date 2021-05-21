from django.contrib import admin

# Register your models here.

from .models import (
    Address,
    ConfigChoice,
    ConfigChoiceCategory,
)


admin.site.register(ConfigChoiceCategory)
admin.site.register(ConfigChoice)
admin.site.register(Address)
