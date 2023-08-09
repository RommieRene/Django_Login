from django.contrib import admin
from .models import Category, Product, Cart, Contact
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']
    search_fields = ['name']

admin.site.register(Cart)
admin.site.register(Contact)

