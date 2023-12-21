from django.contrib import admin
from .models import Drug, User, Clinic, District


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass
