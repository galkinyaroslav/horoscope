from django.contrib import admin
from .models import ZodiacSign, SignHoroscope


# Register your models here.

class ZodiacSignAdmin(admin.ModelAdmin):
    list_display = ('sign_name', 'from_date', 'to_date', 'sign_view', 'sign_image',)
    prepopulated_fields = {'slug': ('sign_name',)}


admin.site.register(ZodiacSign, ZodiacSignAdmin)


class SignHoroscopeAdmin(admin.ModelAdmin):
    list_display = ('sign_horoscope', 'sign', 'date',)
    prepopulated_fields = {'slug': ('date',)}


admin.site.register(SignHoroscope, SignHoroscopeAdmin)
