from django.contrib import admin
from .models import *

admin.site.register(Role)
admin.site.register(BankAccount)
admin.site.register(PersonalData)
admin.site.register(File)
admin.site.register(CustomField)
admin.site.register(CustomFieldValue)
