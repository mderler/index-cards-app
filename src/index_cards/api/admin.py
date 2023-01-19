from django.contrib import admin

from .models import Card, PractiseSession, SessionCard, Topic

# Register your models here.

admin.site.register(Card)
admin.site.register(PractiseSession)
admin.site.register(SessionCard)
admin.site.register(Topic)
