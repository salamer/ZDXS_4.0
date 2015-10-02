from django.contrib import admin
from data.models import Data,DataComment,Category,Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display=['category','category_image']

class DataAdmin(admin.ModelAdmin):
    fields = ('data_category','title','summury','data')
    list_display=['data_category','title','editor','summury']
    search_fields=('editor','data_category',)
    list_filter=('editor','data_category',)
    
class DataCommentAdmin(admin.ModelAdmin):
    list_display=['editor','link']
    list_filter=('link',)
# Register your models here.

admin.site.register(Data,DataAdmin)
admin.site.register(DataComment,DataCommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)