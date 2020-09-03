from django.contrib import admin
from .models import ntpcusers, ntpcvisitors

admin.site.register(ntpcusers)
admin.site.register(ntpcvisitors)

admin.site.site_header = "Clique - Administration"
admin.site.site_title = "Clique"
