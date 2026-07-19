from django.contrib import admin

from cv.models import Experience, Project, Formation, Competence

# Register your models here.

class experiencesAdmin(admin.ModelAdmin):
    list_display = ('poste', 'entreprise', 'start_date', 'end_date', 'image_name', 'published', 'last_updated', 'icon_name')
    list_editable = ('published',)
    list_filter = ('published', 'start_date')
    search_fields = ('poste', 'description', )
    prepopulated_fields = {'slug': ('poste',)}
    date_hierarchy = 'start_date'
    ordering = ['-start_date']

admin.site.register(Experience, experiencesAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published', 'icon',"ordering",)
    list_editable = ('published','ordering','icon',"ordering",)
    list_filter = ('published',)
    search_fields = ('title', 'description', )
    ordering = ("ordering",)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)



class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'year', 'link','certification','published', 'icon_name')
    list_editable = ('certification','published')
    list_filter = ('certification','published')
    search_fields = ('title', 'certification', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Formation, FormationAdmin)



class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'identifier', 'image_name', 'content')
    search_fields = ('title',  )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Competence, CompetenceAdmin)


