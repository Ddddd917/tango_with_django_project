from django.contrib import admin
from rango.models import Category, Page

# Customize the Category admin interface
class CategoryAdmin(admin.ModelAdmin):
    # Automatically populate the slug field based on the name field
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register the models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)