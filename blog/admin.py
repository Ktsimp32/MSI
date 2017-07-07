from django.contrib import admin
from .models import Post, ContactInfo

# Register your models here.
admin.site.register(Post)
admin.site.register(ContactInfo)