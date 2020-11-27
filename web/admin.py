from django.contrib import admin

# Register your models here.
from .models import Network_destination, Source_path,Policy,Policy_process
admin.site.register(Network_destination)
admin.site.register(Source_path)
admin.site.register(Policy)
admin.site.register(Policy_process)
