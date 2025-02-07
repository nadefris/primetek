from django.contrib import admin
from .models import post, Category, comment

class commentItemInline(admin.TabularInline):
    model = comment
    raw_id_fields =['post']

class PostAdmin(admin.ModelAdmin):
    search_fields =['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_on', 'status']
    list_filter = ['category', 'created_on', 'status']
    inlines = [commentItemInline]    
    prepopulated_fields = {'slug': ('title',)}

    
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields =['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
class commmentAdmin(admin.ModelAdmin):
    search_fields =['title', 'intro', 'body']
    list_display = ['name', 'post', 'created_on']

    


# Register your models here.
admin.site.register(post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(comment, commmentAdmin)
