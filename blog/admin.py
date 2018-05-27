from django.db import models
from django.contrib import admin
from markdownx.widgets import AdminMarkdownxWidget

from .models import Post, Category, Tag

# Register your models here.	
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    list_display = ('author', 'title', 'body', 'read_amount','create_time', 'update_time', 'category', 'tags_list')
    filter_horizontal = ('tags',)
    search_fields = ['title', 'body']

    def tags_list(self, post):
        names = map(lambda x: x.name, post.tags.all())
        return ', '.join(names)

    """
    功能同上
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    """

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')	

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
	
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
