from django.contrib import admin

# Register your models here.
from .models import Question, ContactUsForm

admin.site.register(Question)
# admin.site.register(ContactUsForm)
