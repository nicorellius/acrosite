from django.contrib import admin

from .models import Word, Construction, Acrostic


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
    list_display = ['sequence', 'constr_id', ]
    
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
    list_display = ['vertical_word', 'horizontal_words', 'construction_id', 'theme', ]
    
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
            'fields': ('vertical_word', 'horizontal_words', 'construction_id', 'theme',)
        }),
    )

 
# register classes in admin, uses auto_register for apps
admin.site.register(Word, WordAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Acrostic, AcrosticAdmin)