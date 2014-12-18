from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['user', 'organization', 'website', 'phone', 'avatar', ]

    # fields to filter the change list with
    list_filter = ['created', ]

    # fields to search in change list
    search_fields = ['user', ]

    # enable the date drill down on change list
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': ('user', 'organization', 'website', 'phone', 'avatar', )
        }),
    )

# register classes in admin, uses auto_register for apps
admin.site.register(UserProfile, UserProfileAdmin)
