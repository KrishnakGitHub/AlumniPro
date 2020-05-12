from django.contrib import admin
from college.models import Notice
from college.models import Branch
from college.models import Profile

admin.site.register(Branch)
admin.site.register(Profile)


# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_filter = ["cr_date",  "branch"]
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
admin.site.register(Notice, NoticeAdmin)
