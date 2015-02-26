from django.contrib import admin

from .models import Word, Acrostic, Score


class WordAdmin(admin.ModelAdmin):

    list_display = ['name', 'id', 'part_of_speech', 'themes', 'tags', 'name_length', 'valid_name_length', 'valuation', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True
    
    fieldsets = (
        (None, {
            'fields': ('name', 'part_of_speech', 'themes', 'tags', 'name_length', 'valid_name_length', 'valuation',)
        }),
    )


class ScoreInline(admin.StackedInline):
    model = Score

    fields = ('value', )

    
class AcrosticAdmin(admin.ModelAdmin):

    list_display = ['vertical_word', 'id', 'uaid', 'theme_name', 'construction_sequence', 'horizontal_words']
    list_filter = ['created', ]
    search_fields = ['horizontal_words', ]
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {'slug': ('horizontal_words',), }
    
    fieldsets = (
        (None, {
            'fields': ('vertical_word', 'horizontal_words', 'construction_sequence', 'theme_name', 'slug')
        }),
    )

    inlines = [ScoreInline, ]

    def related_score(self, obj):
        return obj.score.value

    related_score.short_description = 'Score'


class ScoreAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['value', 'acrostic', 'mean', 'total', 'created', 'modified', ]
    list_filter = ['created', ]
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('value', )
        }),
    )
 
# register classes in admin, uses auto_register for apps
admin.site.register(Word, WordAdmin)
admin.site.register(Acrostic, AcrosticAdmin)
admin.site.register(Score, ScoreAdmin)