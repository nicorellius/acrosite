from django.contrib import admin

from .models import Word, Acrostic, Score, Construction


class WordAdmin(admin.ModelAdmin):
    
    # fields display on change list
    list_display = ['name', 'part_of_speech', 'tags', 'valuation', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('name', 'part_of_speech', 'tags', 'valuation',)
        }),
    )

    
class ConstructionAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['sequence', 'themes',  'tags', 'type', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('sequence', 'constr_id',)
        }),
    )


class ScoreInline(admin.StackedInline):
    model = Score

    fields = ('value', )

    
class AcrosticAdmin(admin.ModelAdmin):
    
    # fields display on change list
    list_display = ['vertical_word', 'horizontal_words', 'construction', 'theme', 'slug']
    list_filter = ['created', ]
    search_fields = ['horizontal_words', ]
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('horizontal_words',), }
    
    fieldsets = (
        (None, {
            'fields': ('vertical_word', 'horizontal_words', 'construction', 'theme', 'slug')
        }),
    )

    inlines = [ScoreInline, ]

    def related_score(self, obj):
        return obj.score.value

    related_score.short_description = 'Score'


# class ThemeAdmin(admin.ModelAdmin):
#
#     # fields display on change list
#     list_display = ['name', 'group', 'tags', ]
#     list_filter = ['created', ]
#     search_fields = ['name', ]
#     date_hierarchy = 'created'
#     save_on_top = True
#
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'group', 'tags',)
#         }),
#     )


class ScoreAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['value', 'acrostic', 'mean', 'total', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('value', )
        }),
    )
 
# register classes in admin, uses auto_register for apps
admin.site.register(Word, WordAdmin)
admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Acrostic, AcrosticAdmin)
# admin.site.register(Theme, ThemeAdmin)
admin.site.register(Score, ScoreAdmin)