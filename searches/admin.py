from django.contrib import admin

from .models import (
    Hotel,
    HotelImage,
    HotelSpecifications,
    HotelSpecificationValue,
    HotelType,
    HotelAddress,
)


class HotelSpecificationInline(admin.TabularInline):
    model = HotelSpecifications


@admin.register(HotelType)
class HotelTypeAdmin(admin.ModelAdmin):
    inlines = [
        HotelSpecificationInline,
    ]


class HotelImageInline(admin.TabularInline):
    model = HotelImage


class HotelSpecificationValueInline(admin.TabularInline):
    model = HotelSpecificationValue


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelSpecificationValueInline, HotelImageInline]


admin.site.register(HotelAddress)
