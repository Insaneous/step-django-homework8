from django.contrib import admin
from postapp.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at'
    ]
    list_filter = [
        'title',
        'created_at'
    ]

admin.site.register(Post, PostAdmin)