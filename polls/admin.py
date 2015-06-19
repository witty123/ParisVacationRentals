from django.contrib import admin

from .models import Post, Categories, Post_related_images, Index_quick_links
# from .models import Image
# from django.contrib import messages


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
               ('Title', {'fields': ['title']}),
               (None, {'fields': ['is_enabled']}),
               (None, {'fields': ['is_article']}),
               (None, {'fields': ['is_guide']}),
               ('URL', {'fields': ['slug']}),
               ('Date Information', {'fields': ['pub_date']}),
               (None, {'fields': ['updated_date']}),
               ('Text', {'fields': ['body']}),
               ('Category', {'fields': ['categories']}),
               ('Meta', {'fields': ['meta_title']}),
               (None, {'fields': ['meta_description']}),
               (None, {'fields': ['meta_keywords']}),
               (None, {'fields': ['meta_canonical']}),
               ('Quick Links', {'fields': ['quick1', 'quick1_title', 'quick1_image']}),
               (None, {'fields': ['quick2', 'quick2_title', 'quick2_image']}),
               (None, {'fields': ['quick3', 'quick3_title', 'quick3_image']}),
               (None, {'fields': ['quick4', 'quick4_title', 'quick4_image']}),
               ]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date', 'title']
    search_fields = ['title']

class CategoriesAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Description', {'fields': ['info']}),
        ('URL',{'fields':['slug']}),
    ]

class Index_quick_linksAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',{'fields':['title']}),
        (None,{'fields':['current']}),
        ('Quick Links',{'fields':['Iquick1','Iquick1_title','Iquick1_image']}),
        (None,{'fields':['Iquick2','Iquick2_title','Iquick2_image']}),
        (None,{'fields':['Iquick3','Iquick3_title','Iquick3_image']}),
        (None,{'fields':['Iquick4','Iquick4_title','Iquick4_image']}),
    ]

class Post_related_imagesAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Description', {'fields': ['description']}),
        ('Image upload',{'fields':['image','smallimage','largeimage']}),
        ('Post',{'fields':['post']}),
    ]
    #url=image.url
    #def save_model(self, request, obj, form, change):
     #   messages.add_message(request, messages.INFO, 'URL for this image is ')

   
    
admin.site.register(Post, PostAdmin)
admin.site.register(Categories,CategoriesAdmin )
admin.site.register(Post_related_images,Post_related_imagesAdmin)
admin.site.register(Index_quick_links,Index_quick_linksAdmin)
#admin.site.register(Image,ImageAdmin)
# Register your models here.
