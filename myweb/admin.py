from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Staff, Blog, ContactUs

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'date_pub', 'date_updated')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Staff)
admin.site.register(ContactUs)
# Register your models here.
