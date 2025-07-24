from django.contrib import admin
from .models import Post
# Register your models here.
#how the data saved using the post model gonna validate in the admin/blog making it more interactive
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','updated','status']
    list_filter=['author','status','updated','created']
    search_fields=['title','body']
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=['author']
    date_hierarchy='publish'
    ordering=['status','publish']
    show_facets=admin.ShowFacets.ALWAYS #used to show numbers