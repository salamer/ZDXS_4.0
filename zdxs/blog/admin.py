from django.contrib import admin
from blog.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    fields = ('title','summury','body')
    list_display=['title','editor','summury']
    search_fields=('title','editor',)
    list_filter=('editor',)


    

admin.site.register(Blog,BlogAdmin)

