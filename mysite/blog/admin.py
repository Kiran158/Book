from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('book',  'slug', 'status', 'created_on')


admin.site.register(Post, PostAdmin)
