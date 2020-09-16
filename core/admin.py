from django.contrib import admin
from .models import ntpcuser, externaluser, visitor, meeting

admin.site.register(ntpcuser)
admin.site.register(externaluser)
admin.site.register(visitor)
admin.site.register(meeting)

admin.site.site_header = "Clique - Administration"
admin.site.site_title = "Clique"
