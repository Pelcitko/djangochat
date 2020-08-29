from django.contrib import admin

from .models import Contact, Chat, Message

admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)

# from rest_framework.renderers import DocumentationRenderer
#
#
# class CustomRenderer(DocumentationRenderer):
#     languages = ['ruby', 'go']