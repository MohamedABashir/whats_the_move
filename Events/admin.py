from django.contrib import admin

from django.utils import timezone
from django.contrib.auth.models import User

from .models import Category, Event,Comments
from mapbox_location_field.admin import MapAdmin
from django_comments_xtd.admin import XtdCommentsAdmin
class CustomCommentAdmin(XtdCommentsAdmin):
    list_display = ('cid', 'name', 'object_pk','content_type',
                    'ip_address', 'submit_date', 'followup', 'is_public',
                    'is_removed')
    fieldsets = (
        (None, {'fields': ('content_type', 'object_pk', 'site')}),
        ('Content', {'fields': ('user', 'user_name', 'user_email',
                                'user_url', 'comment', 'followup')}),
        ('Metadata', {'fields': ('submit_date', 'ip_address',
                                 'is_public', 'is_removed')}),
    )

admin.site.register(Comments, CustomCommentAdmin)
admin.site.register(Event, MapAdmin)
admin.site.register(Category)




