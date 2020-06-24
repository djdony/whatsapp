from django.contrib import admin, messages
from django.contrib.admin import AdminSite, sites
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext
from datetime import datetime

from .models import Country, Region, CompanyType, Company, City


class CountryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(CountryAdmin, self).get_queryset(request).filter(status=1)

    list_display = list_display_links = ['id', 'code', 'name', 'status']
    exclude = ['status']
    search_fields = ('name',)


class RegionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(RegionAdmin, self).get_queryset(request).filter(status=1)

    list_display = list_display_links = ['id', 'name', 'status', 'country']
    exclude = ['status']
    list_filter = ('status', 'country')
    search_fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(CityAdmin, self).get_queryset(request).filter(status=1)

    list_display = ['id', 'name', 'status', 'region']
    list_display_links = ['id', 'name']
    exclude = ['status']
    list_filter = ('status', 'region')
    list_editable = ('status', 'region')
    search_fields = ('name',)


class CompanyTypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(CompanyTypeAdmin, self).get_queryset(request).filter(status=1)

    list_display = list_display_links = ['id', 'name', 'status']
    exclude = ['status']
    search_fields = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(CompanyAdmin, self).get_queryset(request).filter(status=1)

    list_display = list_display_links = ['id', 'name', 'company_type', 'city', 'whatsapp', 'email', 'www', 'get_logo']
    exclude = ['status']
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['get_logo',  'id']

    def get_logo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src={obj.logo.url} width="50">')
        return '-'

    get_logo.short_description = 'Logo'


def make_active(modeladmin, request, queryset):
    updated = queryset.update(status='1')
    modeladmin.message_user(request, ngettext(
        '%d Item was successfully undeleted.',
        '%d Items was successfully undeleted.',
        updated,
    ) % updated, messages.SUCCESS)


make_active.short_description = "Undelete selected"


def make_disable(modeladmin, request, queryset):
    updated = queryset.update(status='0', modified=datetime.now())
    modeladmin.message_user(request, ngettext(
        '%d Item was successfully deleted.',
        '%d Items was successfully deleted.',
        updated,
    ) % updated, messages.SUCCESS)


make_disable.short_description = "Delete selected"

admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(CompanyType, CompanyTypeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.add_action(make_disable)
admin.site.disable_action('delete_selected')
