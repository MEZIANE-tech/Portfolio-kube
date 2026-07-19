from django.contrib import admin
from Blog.models import BlogSection, CommandeUtile,  Tutoriel

# Register your models here.


@admin.register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'emoji', 'description', 'published','last_updated')
    search_fields = ('title',  )
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(BlogSection, BlogSectionAdmin)


@admin.register(CommandeUtile)
class CommandeUtileAdmin(admin.ModelAdmin):
    list_display = ('title',  'description', 'published', 'last_updated')
    list_display_links = ('title',)
    list_editable = ( 'published',)
    search_fields = ('title', 'published', )
    prepopulated_fields = {'slug': ('title',)}
    
    
@admin.register(Tutoriel)
class TutorielAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published','last_updated')
    list_display_links = ('title',)
    list_editable = ('published',)
    search_fields = ('title', 'published', )
    prepopulated_fields = {'slug': ('title',)}
    

