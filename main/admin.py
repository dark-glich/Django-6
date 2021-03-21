from django.contrib import admin
from .models import Comments, Maths, Science, History, Geography, Civics, Economics

admin.site.site_header = "Solution's Admin Page"

admin.site.register(Comments)
admin.site.register(Maths)
admin.site.register(Science)
admin.site.register(History)
admin.site.register(Economics)
admin.site.register(Civics)
admin.site.register(Geography)