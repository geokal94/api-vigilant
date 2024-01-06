from django.contrib import admin

from .models import Endpoint, TestResult

admin.site.register(Endpoint)
admin.site.register(TestResult)

# Register other models as needed.
