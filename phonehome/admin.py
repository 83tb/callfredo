from django.contrib import admin
from phonehome.models import Call, Recording, Birthday

admin.site.register(Call)
admin.site.register(Birthday)

class RecordingAdmin(admin.ModelAdmin):
    list_display = ('call_sid', 'caller', 'recipient', 'duration', 'url',)

admin.site.register(Recording, RecordingAdmin)

