from django.contrib import admin
from .models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','description','price','available','created']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)