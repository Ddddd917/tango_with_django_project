from django.contrib import admin
from rango.models import Category, Page

# 1. 创建定制类
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# 2. 注册时带上这个类
admin.site.register(Category)
admin.site.register(Page, PageAdmin)