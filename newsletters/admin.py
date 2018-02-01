from django.contrib import admin
from .models import NewsletterUser

# Register your models here.

class NewsletterUserAdmin(admin.ModelAdmin):
	list_display = ('email', 'date_added',)

admin.site.register(NewsletterUser, NewsletterUserAdmin)