# from django.contrib import admin
#
# from apps.search.models import WordListSearch
# from apps.generator.models import Word
#
#
# class SearchWordListInline(admin.TabularInline):
#     model = WordListSearch
#     extra = 3
#
#
# class WordListAdmin(admin.ModelAdmin):
#     model = Word
#     inlines = [SearchWordListInline]
#
#
# admin.site.unregister(Word)
# admin.site.register(Word, WordListAdmin)
