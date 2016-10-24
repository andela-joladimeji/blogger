from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "content"]
    list_display_link = ["updated"]
    list_filter = ["timestamp"]
    list_editables = ["__unicode__"]

    search_fields = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)