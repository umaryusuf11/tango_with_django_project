from django.contrib import admin
from rango.models import Category, Page

# Admin Interface Customizations
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)