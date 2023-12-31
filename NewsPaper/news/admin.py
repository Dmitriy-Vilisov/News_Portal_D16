from django.contrib import admin
from .models import Category, Post


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


nullfy_quantity.short_description = 'Обнулить'


# создаём новый класс для представления админке
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'choice', 'text', 'posting_time')
    list_filter = ('text', 'title')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'author')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
