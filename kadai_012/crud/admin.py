from django.contrib import admin
from .models import Product, Category,Explanation
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price', 'category', 'explanation' ,'image')
     search_fields = ('name',)
     list_filter = ('category',)

     def image(self, obj):
         return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)

class ExplanationAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Explanation, ExplanationAdmin)


