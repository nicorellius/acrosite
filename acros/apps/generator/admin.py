from django.contrib import admin

from .models import Word, Construction, Acrostic, Theme, Score


class WordAdmin(admin.ModelAdmin):

    list_display = ['name', 'part_of_speech', 'themes', 'tags', 'valuation', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('name', 'part_of_speech', 'themes', 'tags', 'valuation',)
        }),
    )

    
class ConstructionAdmin(admin.ModelAdmin):

    list_display = ['sequence', 'themes',  'tags', 'type', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('sequence', 'themes',  'tags', 'type', )
        }),
    )

    
class AcrosticAdmin(admin.ModelAdmin):

    list_display = ['vertical_word', 'horizontal_words', ]
    list_filter = ['created', ]
    search_fields = ['horizontal_words', ]
    date_hierarchy = 'created'
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('vertical_word', 'horizontal_words', )
        }),
    )


class ThemeAdmin(admin.ModelAdmin):

    list_display = ['name', 'group', 'tags', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('name', 'group', 'tags', )
        }),
    )


class ScoreAdmin(admin.ModelAdmin):

    list_display = ['value', 'acrostic', 'user', ]
    list_filter = ['created', ]
    search_fields = ['value', ]
    date_hierarchy = 'created'
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('value', 'acrostic', 'user',)
        }),
    )

 
# register classes in admin, uses auto_register for apps
admin.site.register(Word, WordAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Acrostic, AcrosticAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Score, ScoreAdmin)