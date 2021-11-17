from django.contrib import admin
from .models import (
    Lga,
    States,
    Party,
    Ward,
    AnnouncedWardResults,
    PollingUnit,
    Agentname,
    AnnouncedPuResults,
    AnnouncedLgaResults,
    AnnouncedStateResults,
)
# Register your models here.

admin.site.register(States)
admin.site.register(Lga)
admin.site.register(PollingUnit)
admin.site.register(Party)
admin.site.register(Ward)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedLgaResults)
admin.site.register(Agentname)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedWardResults)
