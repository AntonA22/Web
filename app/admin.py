from django.contrib import admin

from .models import *

admin.site.register(Ship)
admin.site.register(Flight)
admin.site.register(ShipFlight)
