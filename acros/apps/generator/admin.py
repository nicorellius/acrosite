from django.contrib import admin

from .models import Word, Acrostic, Construction, Theme


class WordAdmin(admin.ModelAdmin):
    
    # fields display on change list
    list_display = ['name', 'part_of_speech', 'tags', 'valuation', ]
    
    # fields to filter the change list with
    list_filter = ['created', ]
    
    # fields to search in change list
    search_fields = ['name', ]
    
    # enable the date drill down on change list
    date_hierarchy = 'created'
    
    # enable the save buttons on top on change form
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('name', 'part_of_speech', 'tags', 'valuation',)
        }),
    )

    
class ConstructionAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['sequence', 'themes',  'tags', 'type', ]

    # fields to filter the change list with
    list_filter = ['created', ]

    # fields to search in change list
    search_fields = ['name', ]

    # enable the date drill down on change list
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('sequence', 'constr_id',)
        }),
    )

    
class AcrosticAdmin(admin.ModelAdmin):
    
    # fields display on change list
    list_display = ['vertical_word', 'horizontal_words', 'construction', 'theme', 'score', 'slug']
    
    # fields to filter the change list with
    list_filter = ['created', ]
    
    # fields to search in change list
    search_fields = ['horizontal_words', ]
    
    # enable the date drill down on change list
    date_hierarchy = 'created'
    
    # enable the save buttons on top on change form
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('vertical_word', 'horizontal_words', 'construction', 'theme', 'slug')
        }),
    )


class ThemeAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['name', 'group', 'tags', ]

    # fields to filter the change list with
    list_filter = ['created', ]

    # fields to search in change list
    search_fields = ['name', ]

    # enable the date drill down on change list
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('name', 'group', 'tags',)
        }),
    )
 
# register classes in admin, uses auto_register for apps
admin.site.register(Word, WordAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Acrostic, AcrosticAdmin)
admin.site.register(Theme, ThemeAdmin)