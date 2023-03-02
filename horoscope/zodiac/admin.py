from django.contrib import admin
from .models import ZodiacSigns, SignHoroscope


# Register your models here.

class ZodiacSignsAdmin(admin.ModelAdmin):
    list_display = ('sign_name', 'from_date', 'to_date',)
    prepopulated_fields = {'slug': ('sign_name',)}

admin.site.register(ZodiacSigns,ZodiacSignsAdmin)

class SignHoroscopeAdmin(admin.ModelAdmin):
    list_display = ('sign_horoscope', 'sign', 'date',)
    prepopulated_fields = {'slug': ('date',)}

admin.site.register(SignHoroscope,SignHoroscopeAdmin)