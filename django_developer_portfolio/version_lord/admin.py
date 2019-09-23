from django.contrib import admin
from version_lord.models import Version

class VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Version, VersionAdmin)
