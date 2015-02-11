from django.contrib import admin

from apps.search.models import SearchWordList
from apps.generator.models import Word


class SearchWordListInline(admin.TabularInline):
    model = SearchWordList
    extra = 3


class WordListAdmin(admin.ModelAdmin):
    model = Word
    inlines = [SearchWordListInline]


admin.site.unregister(Word)
admin.site.register(Word, WordListAdmin)
